from core.physiological import PhysiologicalState
from interventions.sound_meditia import SoundMeditia

# Estado inicial
state = PhysiologicalState(heart_rate=110, tension=8)

print("INITIAL STATE:", state)

# Meditia fisiológica (calma)
relax_meditia = SoundMeditia(
    bpm=60,
    rhythm_type="wave",
    intensity=0.3,
    emotional_effect="calm",
    cognitive_effect="selfcare",
    sound_elements=["soft_pads"]
)

# Meditia emocional (alegría)
happy_meditia = SoundMeditia(
    bpm=95,
    rhythm_type="pulse",
    intensity=0.7,
    emotional_effect="happiness",
    sound_elements=["bells"]
)

# Aplicación conceptual (solo demostración simple)
print("\nAPPLYING RELAX MEDITIA...")
print(relax_meditia)

print("\nAPPLYING HAPPY MEDITIA...")
print(happy_meditia)