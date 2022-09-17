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
    
        // Start is called before the first frame update
    void Start()
    {
        
    }

    void Awake()
    {
        current_display = 0;
        linears = new List<classical_story>();
        for (int i=0;i<5; i++)
        {
            classical_story fresh= new classical_story();
            fresh.story = new Story(line_template.text);
            fresh.ForwardFlow();
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
        
    }

    void ShowNext()
    {
        current_display = current_display + 1;
        if (current_display >= linears.Count)
        {
            current_display = 0;
        }
        current_prose.SetText("");
        current_prose.SetText(linears[current_display].AsOneText());


    }


    // Update is called once per frame
    void Update()
    {
        double time_phase = Time.time % (5000 * linears.Count);
        if (time_phase > (5000 * current_display))
        {
            Debug.Log("whoosh");
            ShowNext();
        }
    }
}
