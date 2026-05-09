from dataclasses import dataclass
from typing import Optional, List

@dataclass
class SoundMeditia:
    bpm: Optional[int] = None
    rhythm_type: str = "pulse"
    intensity: float = 0.5

    emotional_effect: Optional[str] = None
    cognitive_effect: Optional[str] = None

    sound_elements: List[str] = None