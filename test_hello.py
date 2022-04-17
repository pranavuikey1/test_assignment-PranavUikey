import hello

def test_hello():
    print('It is working.')
    assert hello.hello_world() == "Hello World!"
    assert "Hello World!" == hello.hello_world()
