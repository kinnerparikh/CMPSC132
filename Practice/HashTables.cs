using System;
using System.Collections.Generic;

namespace Solution
{
    public class CollisionNode
    {
        public int k;
        public Object val;
        public CollisionNode next;
    }

    public class HashTable
    {
        private const int HTSIZE = 100;

        public void Add(int k, Object v)
        {
            int idx = k % HTSIZE;
            CollisionNode entry = new CollisionNode();
            entry.k = k;
            entry.val = v;
            entry.next = ht[idx];
            ht[idx] = entry;
        }

        public bool Exists(int k)
        {
            bool retval = false;
            int idx = k % HTSIZE;
            CollisionNode cur = ht[idx];
            while (cur != null)
            {
                if (cur.k == k)
                {
                    retval = true;
                    break;
                }
                cur = cur.next;
            }
            return retval;
        }

        public Object Get(int k)
        {
            Object retval = null;
            int idx = k % HTSIZE;
            CollisionNode cur = ht[idx];
            while (cur != null)
            {
                if (cur.k == k)
                {
                    retval = cur.val;
                    break;
                }
                cur = cur.next;
            }
            return retval;
        }

        private CollisionNode[] ht = new CollisionNode[HTSIZE];
    }

    public class Solution {
        public static void Main(string[] args)
        {
            List<string> dictionary = new List<string>();

            dictionary.Add("kinner");
            dictionary.Add("elvis");
            dictionary.Add("god");
            dictionary.Add("lives");
            dictionary.Add("sujal");
            dictionary.Add("pot");
            dictionary.Add("dog");
            dictionary.Add("anjali");
            dictionary.Add("hello");
            dictionary.Add("top");
            dictionary.Add("pot");
            dictionary.Add("opt");
            dictionary.Add("odg");

            PrintAnagrams(dictionary);
        }


        // INPUT: kinner, elvis, god, lives, sujal, pot, dog, anjali, hello, top, opt
        // OUTPUT:
        // elvis, lives
        // dog, god
        // pot, top, opt
        public static void PrintAnagrams(List<string> dictionary)
        {
            Dictionary<string, List<string>> ht = new Dictionary<string, List<string>>();
            foreach(string s in dictionary)
            {
                var ca = s.ToCharArray();
                Array.Sort(ca);
                string k = new string(ca);

                if (!ht.ContainsKey(k))
                {
                    List<string> l = new List<string>();
                    ht.Add(k, l);
                }
                ht[k].Add(s);
            }   

            foreach(var k in ht)
            {
                if (k.Value.Count > 1)
                {
                    bool fFirst = true;
                    foreach(var n in k.Value)
                    {
                        if (!fFirst) Console.Write(", ");
                        fFirst = false;
                        Console.Write(n);
                    }
                    Console.WriteLine();
                }
            }
        }

        public static void XMain(string[] args) {
            // you can write to stdout for debugging purposes, e.g.
            Console.WriteLine("This is a debug message");

            HashTable htt = new HashTable();

            htt.Add(10, "Sujal");
            htt.Add(20, "Kinner");
            htt.Add(110, "Anjali"); 
            
            Console.WriteLine(htt.Get(10));
            Console.WriteLine(htt.Get(20));
            Console.WriteLine(htt.Get(110));

            Dictionary<int, String> htc = new Dictionary<int, string>();
            htc.Add(10, "Sujal");
            htc.Add(20, "Kinner");
            htc.Add(110, "Anjali");
            
            Console.WriteLine(htc[10]);
            Console.WriteLine(htc[20]);
            Console.WriteLine(htc[110]);

        }
    }
}
