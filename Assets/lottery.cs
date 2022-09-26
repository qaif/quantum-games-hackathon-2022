using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Lottery
{
    private Dictionary<classical_story,int> occurrences;
    private List<string> pool;
    private List<string> canon;
    public Lottery(string[] puddle)
    {
        pool = new List<string>();
        occurrences = new Dictionary<classical_story,int>();
        canon = new List<string>();
        for (int i=0; i < puddle.Length; i++)
        {
            pool.Add(puddle[i]);
        }
    }

    public string provide(classical_story river)
    {
        if (occurrences.ContainsKey(river))
        {
            occurrences[river] = occurrences[river] + 1;
            if (occurrences[river] > canon.Count)
            {
                int coin = Random.Range(0, pool.Count);
                canon.Add(pool[coin]);
                Debug.Log("coin " + coin.ToString());
            }
            int place = occurrences[river] - 1;
            string content = canon[place];
            foreach (string inspect in canon)
            {
                Debug.Log(inspect);
            }
            Debug.Log("canon" + canon.ToString() + "return " + content);
            foreach (KeyValuePair<classical_story,int> inspect in occurrences)
            {
                Debug.Log(inspect.Value.ToString());
            }
            return content;
        }
        else
        {
            occurrences.Add(river, 0);
            return provide(river);
        }

    }

    public void dupe(classical_story trunk,classical_story branch)
    {
        Debug.Log("dupe");
        Debug.Log(trunk.quantumLord.linears.IndexOf(trunk).ToString());
        Debug.Log(branch.quantumLord.linears.IndexOf(branch).ToString());
        if (occurrences.ContainsKey(trunk))
        {
            if (occurrences.ContainsKey(branch) )
            {
                int amount = occurrences[trunk];
                occurrences[branch]= amount;
            }
            else
            {
                int amount = occurrences[trunk];
                occurrences.Add(branch, amount);
            }
        }
        else
        {
            occurrences.Add(trunk, 0);
            dupe(trunk, branch);
        }
    }
}
