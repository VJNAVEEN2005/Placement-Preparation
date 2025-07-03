import java.util.*;

public class QueueSyntax {
    public static void main(String[] args) {
        Queue<Integer> queue = new LinkedList<>();

        queue.add(1);
        queue.add(2);
        queue.add(3);

        int first = queue.poll();
        queue.poll();
        int peek = queue.peek();

        System.out.println(first);
        System.out.println(peek);

    }
}
