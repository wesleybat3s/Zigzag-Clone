using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BallTransmiter : MonoBehaviour
{
    [SerializeField] private Ball�nput ballInput;

    public Vector3 GetBallDirection()
    {
        return ballInput.ballDirection;
    }
    
}
