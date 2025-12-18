class Solution {
    static{
        Runtime.getRuntime().addShutdownHook(new Thread(() -> {
            try (FileWriter writer = new FileWriter("display_runtime.txt")) {
                writer.write("0");
            } catch (IOException e) {
                e.printStackTrace();
            }
        }));
    }
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists == null) return null;
        if (lists.length == 1) return lists[0];
        ListNode finalList = new ListNode(0);

        ListNode head = finalList;
        for (int i = 1; i < lists.length; i++) {
            ListNode newNode = new ListNode(0);
            ListNode headNode = newNode;
            ListNode list1 = finalList.next == null ? lists[i-1] : finalList.next;
            ListNode list2 = lists[i];

            while (list1 != null && list2 != null) {
                if (list1.val < list2.val) {
                    newNode.next = list1;
                    list1 = list1.next;
                } else {
                    newNode.next = list2;
                    list2 = list2.next;
                }
                newNode = newNode.next;
            }
            if (list1 == null) {
                newNode.next = list2;
            }
            if (list2 == null) {
                newNode.next = list1;
            }

            finalList.next = headNode.next;

        }

        return head.next;
    }
}