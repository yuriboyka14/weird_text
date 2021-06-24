from encoder import Encoder

def test1():
    a = "What a (biiiig) and beautiful automobile! \nWhat a time to be alive!"
    Encoder(a)

def test2():
    a = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s"
    Encoder(a)

def test3():
    a = "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable."
    Encoder(a)