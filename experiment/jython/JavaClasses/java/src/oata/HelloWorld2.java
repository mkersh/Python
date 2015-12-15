package oata;

public class HelloWorld2 {
    public static void main(String[] args) {
    	HelloWorld hw = new HelloWorld();
        System.out.println("Hello" + hw.SayHello());
    }

    public String doit(){
    	// In my test the sayHello should be overriden by a jython class
    	System.out.println("Java doit calling SayHello:" + this.SayHello());
    	return "doit returned";
    }

    public String SayHello(){
    	return "This is HelloWorld2 SayHello()";
    }

    public String SayHello(int i){
    	String str = "This is java SayHello(int)";
    	// These prints are not appearing in Jython. Whereas the doit one above is??
    	System.out.println(str);
    	return str;
    }

    public String SayHello(int i, String s){
    	String str = "This is java SayHello(int, String)";
    	System.out.println(str);
    	return str;
    }
}