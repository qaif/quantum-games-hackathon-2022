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
    
        // Start is called before the first frame update
        void Start()
    {
        
    }

    void Awake()
    {
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

    // Update is called once per frame
    void Update()
    {
        
    }
}
