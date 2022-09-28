using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class QTree : MonoBehaviour
{
    public SpriteRenderer spriteRenderer;
    public Sprite collapsedTree;

    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {

    }

    public void Collapse(bool collapse)
    {
        gameObject.SetActive(collapse);

        if (collapse)
        {
            spriteRenderer.sprite = collapsedTree;
            spriteRenderer.color = Color.white;
        }
    }
}
