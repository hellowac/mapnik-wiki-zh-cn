Here we collect the guidelines and tricks to leverage debugging and logging Mapnik when developing in **the upcoming 2.1.0 release**.

## The runtime logger
TODO

## Logging where it counts when developing in C++
When you develop Mapnik, and need to output log strings that needs to print common info, debug or warning and error strings, then you need to use the newer logger interface. Be sure you have set this option in _config.py_ (or you are building in DEBUG):

```python
ENABLE_LOG = True
```

Then if we have a file called cairo_renderer.cpp and need to debug a string:

```cpp
#include <mapnik/debug.hpp>
...
// here we need to output a string that will be output in DEBUG severity level:
MAPNIK_LOG_DEBUG(cairo_renderer) << "Log my data, visible at DEBUG severity level";
```

## All the logging facilties in C++

```cpp
// Output a string in INFO severity level
MAPNIK_LOG_INFO(object_name) << "This is INFO";

// Output a string in DEBUG severity level
MAPNIK_LOG_DEBUG(object_name) << "This is DEBUG";

// Output a string in WARN severity level
MAPNIK_LOG_WARN(object_name) << "This is WARN";

// Output a string in ERROR severity level
MAPNIK_LOG_ERROR(object_name) << "This is ERROR";

// Output a string in FATAL severity level
MAPNIK_LOG_FATAL(object_name) << "This is FATAL";
```

## Best practices
This has the advantages that it will be optimized automatically by the compiler when ENABLE_LOG is set to False.
But if you need to perform complex code before outputting a string to debug, then it's better to disable those expensive calls completely when log is not enabled:

```cpp
#include <mapnik/debug.hpp>
...
#ifdef MAPNIK_LOG
  // here we need to output a string that will be output in DEBUG severity level:
  const double a = 1.0 / sin(x);
  const double z = a * connection->get_zoom_from_sql_call();
  MAPNIK_LOG_INFO(cairo_renderer) << "Log the variable " << z << ", visible at INFO severity level";
#endif
```