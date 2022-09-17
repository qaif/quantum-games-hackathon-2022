using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
using Ink.Runtime;
using TMPro;

public class test_ink_driver : MonoBehaviour
{

    [SerializeField]
    private TextAsset inkJSONAsset = null;
    public Story story;

    public TextMeshProUGUI text_shower;

    public int lines_happened;
    public double lineswitch_wait_ms;
    public TMP_InputField commander;
    private double next_time_to_proceed;
    private int random_proceeding;

    void Awake()
    {
        // Debug.Log("I am awake");
        commander.onSubmit.AddListener(CommandParsing);
        StartStory();
    }


    public static event Action<Story> OnCreateStory;
    // Start is called before the first frame update
    void Start()
    {
    }

    void CommandParsing(string babble)
    {
        Debug.Log("commanded to: "+babble);
    }


    void ThenThisHappens()
    {
        next_time_to_proceed = lines_happened * (lineswitch_wait_ms*(1.0/1000.0));
        //Debug.Log(next_time_to_proceed.ToString()+ "lines "+ lines_happened.ToString());
        if (next_time_to_proceed < UnityEngine.Time.fixedTime)
        {
            if (story.canContinue)
            {
                string text = story.Continue();
                text_shower.SetText(text);
                //Debug.Log(text);
                lines_happened = lines_happened + 1;
            }
            else
            {
                if (story.currentChoices.Count > 0)
                {
                    for (int i = 0; i < story.currentChoices.Count; i++)
                    {
                        Choice choice = story.currentChoices[i];
                        Debug.Log("Can choose:" + choice.text);
                    }
                    random_proceeding = UnityEngine.Random.Range(0, story.currentChoices.Count);
                    story.ChooseChoiceIndex(random_proceeding);
                }
                else
                {
                    //Debug.Log("story stuck unable to continue");
                }
            }
        }
    }

    void StartStory()
    {
        story = new Story(inkJSONAsset.text);
        if (OnCreateStory != null) OnCreateStory(story);
        // Debug.Log("started");
        ThenThisHappens();
    }

    void FixedUpdate()
    {
        ThenThisHappens();
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
