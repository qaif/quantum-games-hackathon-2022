using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Ink.Runtime;
using TMPro;

public class superposition_manager : MonoBehaviour
{
    public TextAsset line_template;
    private List<classical_story> linears;
    public TMP_InputField commander;
    public int current_display;
    public TextMeshProUGUI current_prose;
    public TextMeshProUGUI current_prose_2;
    public TextMeshProUGUI current_prose_3;
    public TextMeshProUGUI current_prose_4;
    public TextMeshProUGUI current_prose_5;
    public double time_to_keep_stable;
    private double last_rollover;
    private List<string> world_letters;

    public Dictionary<string, Lottery> lotto;
    
        // Start is called before the first frame update
    void Start()
    {
        
    }

    void Awake()
    {
        current_display = 0;
        last_rollover = 0.0;
        world_letters = new List<string>();
        world_letters.Add("A");
        world_letters.Add("B");
        world_letters.Add("C");
        world_letters.Add("D");
        world_letters.Add("E");
        FromTheTop();

    }

    void HeedAction(string word)
    {
        //Debug.Log("start heed");
        foreach (classical_story line in linears)
        {
            //Debug.Log("heed");
            line.HeedAction(word);
        }
        RefreshDisplays();
        commander.ActivateInputField();
    }

    void ShowNext()
    {
        current_display = current_display + 1;
        if (current_display >= linears.Count)
        {
            current_display = 0;
            last_rollover = Time.time;
        }
        int limit = 0;
        while (linears[current_display].the_end_is_here == true && limit<100) {
            current_display = current_display + 1;
            if (current_display >= linears.Count)
            {
                current_display = 0;
                last_rollover = Time.time;
            }
            limit = limit + 1;
        }
        if (limit >= 100)
        {
            EndShow();
        }
        current_prose.SetText("");
        RefreshDisplays();


    }

    void EndShow()
    {
        bool retry_ask = false;
        for (int i=0; i<linears.Count; i++)
        {
            if (linears[i].story.variablesState["retry"].ToString() == "true")
            {
                retry_ask = true;
            }
        }
        commander.onSubmit.RemoveListener(HeedAction);
        if (retry_ask)
        {
            FromTheTop();
        }
        else
        {
            Application.Quit();
            Debug.Log("THE GAME EXITED");
        }
    }

    void FromTheTop()
    {
        lotto = new Dictionary<string, Lottery>();
        string[] dual = new string[] { "true","false"};
        Lottery a = new Lottery(dual,5);
        //Debug.Log(dual);
        Lottery b = new Lottery(dual,5);
        Lottery c = new Lottery(new string[]{"animal","handle with care","express"},5);
        lotto.Add("atomic_fact",a);
        lotto.Add("bomb_fuse",b);
        lotto.Add("box_label", c);

        linears = new List<classical_story>();
        for (int i = 0; i < 5; i++)
        {
            classical_story fresh = new classical_story(this,line_template);
            //fresh.force_add("story "+i.ToString());
            fresh.story.onError += (huuto, what) =>
            {
                catchError(world_letters[i], huuto, what);
            };
            superposition_manager echo_copy = this;
            int j = i;
            fresh.story.BindExternalFunction("coherentLottery", (string ticket) => {
                Debug.Log("inside bind");
                Debug.Log(ticket);
                Debug.Log(linears.Count.ToString());
                Debug.Log(i);
                Debug.Log(j);
                string midway = echo_copy.CoherentLottery(linears[j], ticket);
                return midway;
            });
            fresh.ForwardFlow();
            fresh.story.variablesState["world"] = world_letters[i];
            linears.Add(fresh);
            //Debug.Log("plop");

        }
        //HeedAction("test");
        commander.onSubmit.AddListener(HeedAction);
        RefreshDisplays();
        commander.ActivateInputField();
    }


    void RefreshDisplays()
    {
        string payload = linears[current_display].AsOneText();
        current_prose.SetText(payload);
        current_prose_2.SetText(payload);
        current_prose_3.SetText(payload);
        current_prose_4.SetText(payload);
        current_prose_5.SetText(payload);
    }

    void catchError(string storyid,string huuto, Ink.ErrorType what)
    {
        Debug.Log("story "+storyid+" "+what.ToString() + " : " + huuto);
    }

    public string CoherentLottery(classical_story river,string lotterytype)
    {
        for (int i=0; i < linears.Count; i++)
        {
            if (linears[i] == river)
            {
                string result= lotto[lotterytype].provide(i);
                Debug.Log(result + " " + i);
                return result;
            }
        }
        Debug.Log("failed to identify lottery");
        return "The player is not supposed to see this";
    }


    // Update is called once per frame
    void Update()
    {
        double time_phase = Time.time - last_rollover;
        //Debug.Log(time_phase+ (time_to_keep_stable * (current_display+1)).ToString());
        if (time_phase > (time_to_keep_stable * (current_display+1)))
        {
            //Debug.Log("whoosh");
            ShowNext();
        }
    }
}
