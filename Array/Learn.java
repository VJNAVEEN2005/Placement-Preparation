public class Learn {

    public static void main(String[] args) {

        int[][] arr = {
            {1, 2, 3},
            {4, 5},
            {7, 8, 9}
        };

        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.print("\n");
        }
        // System.out.println(Arrays.toString(arr));
    }
}
