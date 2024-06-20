class A:
    def method(self):
        print("A class")
        super().method()
class B:
    def method(self):
        print("B class")
        super().method()
class C(B,Ag):
    def method(self):
        print("C class")
        super().method()
object=C()
object.method()