<!-- Name: BuildBot -->
<!-- Version: 9 -->
<!-- Last-Modified: 2009/10/18 14:54:16 -->
<!-- Author: springmeyer -->
## Mapnik BuildBot

### How it works

Mapnik developer Beau Gunderson hosts a "master" buildbot instance here:

http://miranda.nwcr.net:8010/waterfall

This instance watches Mapnik svn for new commits and re-builds mapnik with each code change.

Currently on the main 'miranda' server we have both a "slave" that tests Mapnik compile/build/tests on freebsd and another that does it Ubuntu8.10

### Setting up a new Slave

If you have a machine that has good network connectivity and at least 500 MB available ram (no static IP needed) then adding it as a "slave" is easy:

We are looking for all possible unix, linux, and mac osx flavors and various boost versions (especially 1_34 and the latest releases)

Install buildbot:


    # or use package management...
    # easy_install twisted
    # easy_install buildbot
    # easy_install nose

Add a unix user called 'mapnikslave':

    # adduser mapnikslave

Email Beau (beau - at - beaugunderson.com) with your desired <slave name> (essentially a username),<password>, and desired 'Builder' name.

Builder names should be descriptive, like 'springmeyer-Ubuntu-8.10-i686', including something like 'person-platform-version-arch'.

Beau will set up a 'Builder' record for you that is associated with your slavename/password.

Then create this instance (you can also do this before and edit the details later):

    # buildbot create-slave /home/mapnikslave/Buildbot miranda.nwcr.net:9989 <slave name> <password>

This will create a Buildbot folder and config files that look like:


    $ more Buildbot/buildbot.tac 
    
    from twisted.application import service
    from buildbot.slave.bot import BuildSlave
    
    basedir = r'/home/mapnikslave/Buildbot'
    buildmaster_host = 'miranda.nwcr.net'
    port = 9989
    slavename = 'SLAVENAME'
    passwd = 'PASSWORD'
    keepalive = 60
    usepty = 1
    umask = None
    
    application = service.Application('buildslave')
    s = BuildSlave(buildmaster_host, port, slavename, passwd, basedir,
                   keepalive, usepty, umask=umask)
    s.setServiceParent(application)

To start the server then do:


    cd ~/
    buildbot start Buildbot

This process should daemonize (and talk with the master) and you'll only need to restart it when you reboot

## To Do

Currently the Master setup is a bit hardcoded and requires a 'user' named 'mapnikslave' in a /home directory common on linux.

But, this does not work for systems without /home directories (like OS X), so we need to investigate making the primary build master config a bit more flexible (http://buildbot.net/trac/ticket/541)

Also, it would be cool to be able to kick off, and get results back from #mapnik irc.

Currently the 'master.cfg'  looks like:


    If you can figure out a way to have buildbot put the files in the same
    place on both our machines without specifying it like that I would be
    more than willing to set it up!
    
    I will attach the current 'master.cfg' for the build master--have a
    look and see if there's anything we can add to the build to make a
    relative path work, maybe? I tried that and scons installed files
    relative to where they were compiled from and not from a single
    directory relative to the path scons was run from.
    
    Here it is:
    
    c = BuildmasterConfig = {}
    
    ####### BUILDSLAVES
    
    from buildbot.buildslave import BuildSlave
    c['slaves'] = [
            BuildSlave("miranda", "SECRET", max_builds=2),
            BuildSlave("dane", "SECRET", max_builds=2),
    ]
    
    c['slavePortnum'] = 9989
    
    ####### CHANGESOURCES
    
    svnroot = "http://svn.mapnik.org/trunk/"
    
    from buildbot.changes.pb import PBChangeSource
    from buildbot.changes.svnpoller import SVNPoller
    c['change_source'] = [PBChangeSource(), SVNPoller(svnurl=svnroot,
    pollinterval=60*10, svnbin="/usr/local/bin/svn")]
    
    ####### SCHEDULERS
    
    from buildbot.scheduler import Scheduler
    c['schedulers'] = []
    c['schedulers'].append(Scheduler(name="all", branch=None,
                                     treeStableTimer=5*60,
                                     builderNames=["mapnik-freebsd"]))
    
    ####### BUILDERS
    
    from buildbot.process import factory
    from buildbot.steps.source import SVN
    from buildbot.steps.shell import Compile, Configure, Test,
    WarningCountingShellCommand, ShellCommand
    
    class Install(WarningCountingShellCommand):
            name = "install"
            haltOnFailure = 1
            flunkOnFailure = 1
            description = ["installing"]
            descriptionDone = ["installed"]
    
    import os
    
    f1 = factory.BuildFactory()
    
    f1.addStep(SVN(svnurl=svnroot))
    f1.addStep(Configure(command=["python", "scons/scons.py", "configure",
    "INPUT_PLUGINS=all", "COLOR_PRINT=false",
    "PYTHON_PREFIX=/home/mapnikslave/install",
    "PREFIX=/home/mapnikslave/install"]))
    f1.addStep(Compile(command=["python", "scons/scons.py"]))
    f1.addStep(Install(command=["python", "scons/scons.py", "install"]))
    f1.addStep(Test(command=["python", "tests/run_tests.py",
    "--prefix=/home/mapnikslave/install"]))
    
    b1 = {
        'name': "mapnik-freebsd",
        'slavename': "miranda",
        'builddir': "freebsd",
        'factory': f1,
        'env': { 'LD_LIBRARY_PATH': '/home/mapnikslave/install/lib' }
    }
    
    b2 = {
        'name': "mapnik-linux",
        'slavename': "dane",
        'builddir': "linux",
        'factory': f1,
        'env': { 'LD_LIBRARY_PATH': '/home/mapnikslave/install/lib' }
    }
    
    c['builders'] = [b1, b2]
    
    ####### STATUS TARGETS
    
    c['status'] = []
    
    from buildbot.status import html
    c['status'].append(html.WebStatus(http_port=8010, allowForce=True))
    
    # from buildbot.status import mail
    # c['status'].append(mail.MailNotifier(fromaddr="buildbot@localhost",
    #                                      extraRecipients=["builds@example.com"],
    #                                      sendToInterestedUsers=False))
    #
    # from buildbot.status import words
    # c['status'].append(words.IRC(host="irc.example.com", nick="bb",
    #                              channels=["#example"]))
    #
    # from buildbot.status import client
    # c['status'].append(client.PBListener(9988))
    
    ####### DEBUGGING OPTIONS
    
    #c['debugPassword'] = "mapmapbuild"
    
    ####### PROJECT IDENTITY
    
    c['projectName'] = "Mapnik"
    c['projectURL'] = "http://www.mapnik.org/"
    
    c['buildbotURL'] = "http://miranda.nwcr.net:8010/"