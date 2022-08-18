using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GroundCollision : MonoBehaviour
{
    [SerializeField] private GroundTransmitter groundTransmitter;


    private void OnCollisionExit(Collision other)
    {
        if (other.gameObject.CompareTag("Ball"))
        {
            groundTransmitter.SetGroundRigitbodyValue();
        }
    }
}
