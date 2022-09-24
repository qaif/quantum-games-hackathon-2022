using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Lottery
{
    private List<int> occurrences;
    private List<string> pool;
    private List<string> canon;
    public Lottery(string[] puddle,int width=0)
    {
        pool = new List<string>();
        occurrences = new List<int>();
        canon = new List<string>();
        for (int i=0; i < puddle.Length; i++)
        {
            pool.Add(puddle[i]);
        }
        for (int i=0; i < width; i++)
        {
            occurrences.Add(0);
        }
    }

    public string provide(int river)
    {
        occurrences[river] = occurrences[river] + 1;
        if (occurrences[river] > canon.Count)
        {
            float coin = Random.Range(0, 1);
            if (coin > 0.5)
            {
                canon.Add(pool[0]);
            }
            else
            {
                canon.Add(pool[1]);
            }
        }
        int place = occurrences[river]-1;
        string content = canon[place];
        return content;

    }
}
