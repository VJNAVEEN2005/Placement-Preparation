
import java.util.Stack;

public class StackSyntax {
    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<>();

        stack.push(10);
        stack.push(20);
        stack.push(30);

        int top = stack.pop();

        int peek = stack.peek();

        boolean isEmpty = stack.isEmpty();

        System.out.println("Popped element : " + top);
        System.out.println("Top elemet : " + peek);

        System.out.println("Stack is not Empty : "+isEmpty);

    }
}