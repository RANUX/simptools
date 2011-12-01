About
============
Simptools is a suit with useful functions for daily usage.

Dependencies
============
See requirements file::

    pip install -r requirements

Installation
============
Installation from github::

    pip install -e git+https://github.com/RANUX/simptools#egg=simptools

DictObject
============
DictObject is useful when you need to convert dictionary to object.::

    from simptools.dict2object import DictObject

    obj=DictObject({ 'a':'1', 'b':'test'}, {'a': {'type': int}})
    obj.a
    obj.b

Example from simple django view function::

    from simptools.dict2object import DictObject

    def hello_view(request):
        GET = DictObject(request.GET)
        return render_to_response('hello.html', {'name': GET.name})

class_factory
============
Dynamically loads class::

    EmptyClass = class_factory('tests.classes.EmptyClass')
    empty_cls = EmptyClass()

decimals
============
Useful function for working with decimals.

For financial applications::

    >>> two_places_round_up(10.00001)   # result Decimal('10.01')
    >>> two_places_round_down(10.00001) # result Decimal('10.00')

Testing
============
Go to simptools directory and run tests::

    nosetests --all-modules --nologcapture --verbosity=2


Contributing
============
The source is available on `GitHub <http://github.com/RANUX/simptools>`_ - to
contribute to the project, fork it on GitHub and send a pull request, all
contributions and suggestions are welcome!