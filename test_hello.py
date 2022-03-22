import hello;

def test_hello():
    print('It is working.')
    assert hello.hello_world() == "Hello World!"
    assert "Hello!" == hello.hello_world()
