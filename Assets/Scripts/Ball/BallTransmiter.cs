using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BallTransmiter : MonoBehaviour
{
    [SerializeField] private Ballýnput ballInput;

    public Vector3 GetBallDirection()
    {
        return ballInput.ballDirection;
    }
    
}
