using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GroundTransmitter : MonoBehaviour
{
    [SerializeField] private GroundFall groundFall;

    public void SetGroundRigitbodyValue()
    {
        StartCoroutine(groundFall.SetRigitbodyValue());
    } 



    
}
