About
============
Simptools is a suit with useful functions for daily usage.

Dependencies
============
See requirements file.
pip install -r requirements

DictObject
============
DictObject is useful when you need to convert dictionary to object.

    from simptools.dict2object import DictObject

    obj=DictObject({ 'a':'1', 'b':'test'}, {'a': {'type': int}})
    obj.a
    obj.b

Example from simple django view function:

    from simptools.dict2object import DictObject

    def hello_view(request):
        GET = DictObject(request.GET)
        return render_to_response('hello.html', {'name': GET.name})

Testing
============
Go to simptools directory and run tests:
nosetests --all-modules --nologcapture --verbosity=2


Contributing
============
The source is available on `GitHub <http://github.com/RANUX/simptools>`_ - to
contribute to the project, fork it on GitHub and send a pull request, all
contributions and suggestions are welcome!