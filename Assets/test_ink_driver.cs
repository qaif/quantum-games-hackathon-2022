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

    void Awake()
    {
        Debug.Log("I am awake");
        // Remove the default message
        StartStory();
    }


    public static event Action<Story> OnCreateStory;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    void ThenThisHappens()
    {
        string text = story.Continue();
        text_shower.SetText(text);
        Debug.Log(text);
    }

    void StartStory()
    {
        story = new Story(inkJSONAsset.text);
        if (OnCreateStory != null) OnCreateStory(story);
        Debug.Log("started");
        ThenThisHappens();
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
