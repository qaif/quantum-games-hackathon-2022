using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class WinLevel : MonoBehaviour
{
    public SpriteRenderer spriteRenderer;
    public float rate = 2f;
    public float alpha = 0.75f;
    public GameObject winText;
    public bool finalLevel = false;
    public string sceneToLoad;

    private float hue = 0f;

    // Start is called before the first frame update
    void Start()
    {
    }

    // Update is called once per frame
    void Update()
    {
        Color colour = Color.HSVToRGB(hue, 1f, 1f);
        colour.a = alpha;
        spriteRenderer.color = colour;
        hue += Time.deltaTime * rate;
        hue %= 1f;
    }

    public void Activate()
    {
        if (finalLevel)
        {
            winText.SetActive(true);
        }
        else
        {
            SceneManager.LoadScene(sceneToLoad);
        }
    }
}
