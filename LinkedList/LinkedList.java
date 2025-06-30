class Node {

    int data;
    Node next;

    Node(int data) {
        this.data = data;
        next = null;
    }
}

public class LinkedList {

    public static void main(String[] args) {
        Node head = new Node(10);
        Node second = new Node(20);
        Node third = new Node(30);

        head.next = second;
        second.next = third;

        Node current = head;
        while(current != null){
            System.out.println(current.data + "->");
            current = current.next;
        }

        System.out.println("null");
    }
}
