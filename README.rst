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

money extension
============
moneyed.Money extension.

Example::

    >>> from simptools.money import Money, round_down, round_up
    >>> import moneyed
    >>> round_up(Money(10.0001, moneyed.RUB))  # result 10.01 RUB
    >>> round_down(Money(10.0001, moneyed.RUB))  # result 10.00 RUB


test_catch_and_log_exception
============================
Wraps try-except block and log it

Example::

    @catch_and_log_exception(return_expression=-1)
    def div_by_zero(self):
        return 1/0

return_expression - will leave the current function call with the expression list (or None) as return value.

Testing
============
Go to simptools directory and run tests::

    nosetests --all-modules --nologcapture --verbosity=2


Release notes
=============

- 0.6
  - simptools.http HttpClient wrapper over requests.

- 0.5
  - simptools.decorators.catch_and_log_exception added

- 0.4
  - simptools.decimals removed

Contributing
============
The source is available on `GitHub <http://github.com/RANUX/simptools>`_ - to
contribute to the project, fork it on GitHub and send a pull request, all
contributions and suggestions are welcome!