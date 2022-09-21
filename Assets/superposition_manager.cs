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
        foreach (classical_story line in linears)
        {
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
        linears = new List<classical_story>();
        for (int i = 0; i < 5; i++)
        {
            classical_story fresh = new classical_story();
            fresh.story = new Story(line_template.text);
            //fresh.force_add("story "+i.ToString());
            fresh.story.onError += (huuto, what) =>
            {
                catchError(world_letters[i], huuto, what);
            };
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
