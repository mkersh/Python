package oata;

public class HelloWorld {
    public static void main(String[] args) {
    	HelloWorld hw = new HelloWorld();
        System.out.println("Hello World This is MK" + hw.SayHello());
    }

    public String SayHello(){
    	return "Hello this is a Java Class";
    }
}