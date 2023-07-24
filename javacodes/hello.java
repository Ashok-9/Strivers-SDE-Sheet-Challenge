
class Baseclass {
    int x = 20;
    
    void msg() {
        System.out.println("Base class method");
    }
}

class Childclass extends Baseclass {
    int x = 50;
    int y = 100;
    
    void msg() {
        System.out.println("Child class first method");
    }
}

public class hello extends Childclass {
    public static void main(String[] args) {
        Baseclass obj2 = new Childclass();
        System.out.println("Value of x: " + obj2.x);
        obj2.msg();
    }
}