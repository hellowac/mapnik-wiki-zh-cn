<!-- Name: DeveloperTodo -->
<!-- Version: 10 -->
<!-- Last-Modified: 2009/12/11 12:21:41 -->
<!-- Author: springmeyer -->
*Mapnik features that need fixing* (also see the Tickets page):

If you have a plan for any of these items, remove them from here and add them as tickets!

## Python bindings
 * Project is in need of a set of visual unit tests

## Code/API Documentation
 * More C++ classes and parameters need to be documented!
 * We need to generate Doxygen output

## Unexpected behavior

 * "Nil" extents don't work as one might expect (they are initialized to have negative length and negative width, but do not properly support expand_to_include etc.)

## Wishlist
 * Ruby binding :)
 * Mixed imperative / declarative DSL (domain-specific language) for mapping, in the spirit of jQuery, Rails, or Haml-quality design