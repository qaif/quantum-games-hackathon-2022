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
    public double time_to_keep_stable;
    private double last_rollover;
    
        // Start is called before the first frame update
    void Start()
    {
        
    }

    void Awake()
    {
        current_display = 0;
        last_rollover = 0.0;
        linears = new List<classical_story>();
        List<string> world_letters = new List<string>();
        world_letters.Add("A");
        world_letters.Add("B");
        world_letters.Add("C");
        world_letters.Add("D");
        world_letters.Add("E");
        for (int i=0;i<5; i++)
        {
            classical_story fresh= new classical_story();
            fresh.story = new Story(line_template.text);
            fresh.force_add("story "+i.ToString());
            fresh.ForwardFlow();
            fresh.story.variablesState["world"] = world_letters[i];
            linears.Add(fresh);
            Debug.Log("plop");

        }
        HeedAction("test");
        commander.onSubmit.AddListener(HeedAction);
    }

    void HeedAction(string word)
    {
        foreach (classical_story line in linears)
        {
            line.HeedAction(word);
        }
        current_prose.SetText(linears[current_display].AsOneText());
    }

    void ShowNext()
    {
        current_display = current_display + 1;
        if (current_display >= linears.Count)
        {
            current_display = 0;
            last_rollover = Time.time;
        }
        current_prose.SetText("");
        current_prose.SetText(linears[current_display].AsOneText());


    }


    // Update is called once per frame
    void Update()
    {
        double time_phase = Time.time - last_rollover;
        Debug.Log(time_phase+ (time_to_keep_stable * (current_display+1)).ToString());
        if (time_phase > (time_to_keep_stable * (current_display+1)))
        {
            Debug.Log("whoosh");
            ShowNext();
        }
    }
}
