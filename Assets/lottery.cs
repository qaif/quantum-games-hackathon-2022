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
            int coin = Random.Range(0, pool.Count);
            canon.Add(pool[coin]);
            Debug.Log("coin " + coin.ToString());
        }
        int place = occurrences[river]-1;
        string content = canon[place];
        Debug.Log("canon" + canon.ToString()+ "return "+content);
        return content;

    }
}
