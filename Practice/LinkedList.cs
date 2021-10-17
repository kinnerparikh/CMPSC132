using System;

namespace Solution
{
    public class Solution 
    {
        public static void Main(string[] args) 
        {
            byte b = 0x77;

            Console.WriteLine ("Hex: {0:X}", b);
            // Console.WriteLine ("Dec: {0:}", b);

            //b = (byte)~b;
            Console.WriteLine ("Hex: {0:X}", b);
            // Console.WriteLine ("Dec: {0:}", b);

            b = (byte)(b & 3);
            Console.WriteLine ("Hex: {0:X}", b);
        }

        public static void YMain(string[] args) 
        {
            Node h1 = null;
            h1 = Ins(h1, 20);
            h1 = Ins(h1, 201);
            h1 = Ins(h1, 20);
            h1 = Ins(h1, 120);
            h1 = Ins(h1, 220);
            h1 = Ins(h1, 50);
            h1 = Ins(h1, 70);
            PrintList(h1);

            Node h2 = null;
            h2 = Ins(h2, 24);
            h2 = Ins(h2, 241);
            h2 = Ins(h2, 20);
            h2 = Ins(h2, 124);
            h2 = Ins(h2, 224);
            h2 = Ins(h2, 54);
            h2 = Ins(h2, 74);
            h2 = Ins(h2, 740);
            h2 = Ins(h2, 7400);
            h2 = Ins(h2, 7400);
            h2 = Ins(h2, 740);
            h2 = Ins(h2, 745);
            h2 = Ins(h2, 746);
            PrintList(h2);

            Node h = Merge(h1, h2);
            PrintList(h);
        }

        public static void XMain(string[] args) {
            // you can write to stdout for debugging purposes, e.g.
            Console.WriteLine("This is a debug message");

            Node h = null;
            h = Rev(h);
            h = Del(h, 23);
            h = Ins(h, 20);
            h = Rev(h);
            h = Ins(h, 50);
            h = Ins(h, 25);
            h = Ins(h, 100);
            h = Ins(h, 100);
            h = Ins(h, 20);
            h = Ins(h, 43);
            h = Ins(h, 43);
            
            h = Rev(h);
            h = Rev(h);

            h = Del(h, 75);
            h = Del(h, 20);
            h = Del(h, 100);
            h = Del(h, 43);
            h = Del(h, 25);
            h = Del(h, 20);
            h = Del(h, 50);
            h = Del(h, 75);

            h = Ins(h,53);
        }

        public static Node Ins(Node head, int value)
        {
           // Console.WriteLine("Inserting value: " + value);
            head = Insert(head, value);
            //PrintList(head);
            //Console.WriteLine("");
            return head;
        }

        public static Node Del(Node head, int value)
        {
            Console.WriteLine("Deleting value: " + value);
            head = DeleteAll(head, value);
            PrintList(head);
            Console.WriteLine("");
            return head;
        }

        public static Node Rev(Node head)
        {
            Console.WriteLine("Reversing list");
            head = Reverse(head);
            PrintList(head);
            Console.WriteLine("");
            return head;
        }
        
        // print in the following fashion: 10, 12, 18, 200 <newline>
        public static void PrintList(Node head)
        {
            Node temp = head;            
            while (temp != null)
            {
                Console.Write(temp.value);
                if (temp.next != null)
                {
                    Console.Write(", ");
                }
                temp = temp.next;
            } 
            Console.WriteLine("<end>");
        }

        public static Node Merge(Node h1, Node h2)
        {
            Node retVal = null;
            //h1 is empty
            if (h1 == null)
            {
                retVal = h2;
            }
            else if (h2 == null)
            {
                retVal = h1;
            }
            else
            {
                Node curr = null;

                Node currh1 = h1;
                Node nexth1 = h1.next;
                Node currh2 = h2;
                Node nexth2 = h2.next;

                while (currh1 != null && currh2 != null)
                {
                    Node nextToInsert;
                    if (currh1.value < currh2.value)
                    {
                        nextToInsert = currh1;
                        currh1 = currh1.next;
                    }
                    else
                    {
                        nextToInsert = currh2;
                        currh2 = currh2.next;
                    }

                    if (curr == null)
                    {
                        curr = nextToInsert;
                        retVal = curr;
                    }
                    else
                    {
                        curr.next = nextToInsert;
                        curr = curr.next;
                    }
                }
                if (currh1 == null)
                {
                    curr.next = currh2; 
                }
                else if (currh2 == null)
                {
                    curr.next = currh1; 
                }
/*
                if (currh1.value < currh2.value)
                {
                    if (nexth1 == null)
                    {
                        h1.next = h2;
                        retVal = h2;
                    }
                    else
                    {
                        while (nexth1 != null && currh2 != null)
                        {
                            if (currh1.value <= currh2.value && nexth1.value >= currh2.value)
                            {
                                nexth2 = currh2.next;
                                currh1.next = currh2;
                                currh2.next = nexth1;

                                currh1 = currh2;
                                currh2 = nexth2;
                            }
                            else
                            {
                                
                            }
                        }
                    }
                }
*/
            }
            //h2 is empty

            return retVal;
        }

        public static Node Reverse(Node head)
        {
            Node retVal = null;
            // linked list size 0 and 1
            if (head == null || head.next == null)
            {
                retVal = head;
            }
            else
            {
                Node prev = null;
                Node curr = head;
                Node next = head.next;
                while (next != null)
                {
                    curr.next = prev;

                    prev = curr;
                    curr = next;
                    next = next.next;
                }
                curr.next = prev;
                retVal = curr;
            }

            return retVal;
        }

        public static Node Delete(Node head, int value)
        {
            Node retVal = null;

            // head is null case
            if (head == null)
            {
                retVal = null;
            }
            // delete first node
            else if (head.value == value)
            {
                head = head.next;
                retVal = head;
            }
            else 
            {
                Node prev = head;
                Node curr = head.next;

                while (curr != null)
                {
                    if (curr.value == value)
                    {
                        break;
                    }
                    prev = curr;
                    curr = curr.next;
                }
                if (curr != null)
                {
                    prev.next = curr.next;
                }
                retVal = head;
            }
            
            return retVal;
        }

        public static Node DeleteAll(Node head, int value)
        {
            Node retVal = null;

            // head is null case
            if (head == null)
            {
                retVal = null;
            }
            // delete first node
            else if (head.value == value)
            {
                while (head != null && head.value == value)
                {
                    head = head.next;
                }
                retVal = head;
            }
            else 
            {
                Node prev = head;
                Node curr = head.next;

                while (curr != null && curr.value <= value)
                {
                    if (curr.value == value)
                    {
                        curr = curr.next;
                        prev.next = curr;
                    }
                    else
                    {
                        prev = curr;
                        curr = curr.next;
                    }
                }
                retVal = head;
            }
            
            return retVal;
        }

        public static Node Insert(Node head, int value)
        {
            Node retVal = null;

            Node temp = new Node();
            temp.value = value;
            temp.next = null;

            if (head == null)
            {
                retVal = temp;
            }
            else if (value < head.value)
            {
                retVal = temp;
                retVal.next = head;
            }
            else
            {
                Node prev = head;
                Node curr = head.next;
                while (curr != null)
                {
                    if (value < curr.value)
                    {
                        break;
                    }

                    // moving era forward
                    prev = curr;
                    curr = curr.next;
                }
                    
                prev.next = temp;
                temp.next = curr;
                retVal = head;
            }

            return retVal;
        }

        // returns Node because 
        public static Node XInsert(Node head, int value)
        {
            Node temp = new Node();
            temp.value = value;
            
            if (head == null)
            {
                return temp;
            }

            // low to high
            if (value < head.value) 
            {
                temp.next = head;
                return temp;
            }
            else 
            {
                Node curr = head;
                while (value > curr.value && curr.next != null)
                {
                    if (curr.next.value < value)
                    {
                        break;
                    }
                    curr = curr.next;
                }
                temp.next = curr.next;
                curr.next = temp;

                return head;
            }
        }
    }

    public class Node 
    {
        public int value;
        public Node next;
    }

}


// sorted linked list
// isert into linked list

