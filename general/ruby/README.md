# Ruby and Crystal
This folder has small programs written in Ruby and Crystal.

Crystal is a statically typed and compiled language that is almost identical to Ruby. But
because it is statically typed a lot of errors are reported at compile time rather than runtime,
and because it's compiled (based on LLVM) it's actually pretty fast.

## Pros and Cons of Ruby
Ruby is a popular and well established langugae. Documentation is great and getting help is easy.
Performance is a pretty huge bottle neck, but not all applications need to be very performant.
In addition, a lot of applications are limited by I/O rather than raw performance - for example if
you're fetching a bunch of files over the network.

Because it's well established it also has a fairly rich ecosystem built around it with various
libraries and such.

## Pros and Cons of Crystal
Crystal is a lesser known language. The documentation seems OK from what I've seen so far, but
if you run into an issue you can't solve on your own you're fucked (though there probably are
some friendly communities out there who can help). Despite similarities to Ruby it's also not
Ruby, so you won't be able to run Ruby libraries in it.

That said, it's mostly up from here. It's statically typed, so you won't get fucked by trivial
type issues. It's compiled which allows it to run hell of a lot faster than Ruby does.

## How much faster?
Here's a comparison of my two (almost identical) implementations of `decimal_time`, running
5000 times.

```
( repeat 5000; do; ./decimal_time > /dev/null; done; )  5.68s user 2.32s system 127% cpu 6.287 total

( repeat 5000; do; ruby ./decimal_time.rb > /dev/null; done; )  169.33s user 21.76s system 99% cpu 3:11.30 total
```

For something like `editorrenamer` this kind of performance difference doesn't really matter,
but `decimal_time` is something I have running in my status bar and as such performance does
matter.
