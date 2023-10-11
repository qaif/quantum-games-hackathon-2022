using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Measurement : MonoBehaviour
{
    public QuantumState stateToMeasure;

    // Start is called before the first frame update
    void Start()
    {
    }

    // Update is called once per frame
    void Update()
    {
    }

    public void CollapseTrees()
    {
        stateToMeasure.CollapseTrees();
    }
}
