import java.util.Arrays;

public class Relative_Sort_Array_1122 {

    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        // 保存当前有序位置
        int cursor = 0;
        int len = arr1.length;

        for (int term : arr2) {
            for (int i = cursor; i < len; i++) {
                // 冒泡冒上来
                if (arr1[i] == term) {
                    int temp = arr1[cursor];
                    arr1[cursor] = arr1[i];
                    arr1[i] = temp;
                    cursor++;
                }
            }
        }
        Arrays.sort(arr1, cursor, len);

        return arr1;
    }

    public static void main(String[] args) {
        int[] arr1 = {2,3,1,3,2,4,6,20,9,2,19};
        int[] arr2 = {2,1,4,3,9,6};
        int[] r = new Relative_Sort_Array_1122().relativeSortArray(arr1, arr2);
        for (int i : r) {
            System.out.println(i);
        }
    }
}
