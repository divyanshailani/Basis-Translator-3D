import numpy as np

# ==========================================
# 🌌 THE 4 UNIVERSES (Basis Matrices 'P')
# ==========================================

# 1. Standard Lab Frame (Our Reality)
standard = np.array([
    [1.0, 0.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, 0.0, 1.0]
], dtype=float)

# 2. Rotated Universe (45° around Z) — alien thinks "Forward" is diagonal
cos45 = np.cos(np.radians(45))
sin45 = np.sin(np.radians(45))
rotated_z45 = np.array([
    [cos45, -sin45, 0.0],
    [sin45,  cos45, 0.0],
    [0.0,    0.0,   1.0]
], dtype=float)

# 3. Stretched Universe — X twice as long, Y squished to half
stretched = np.array([
    [2.0, 0.0, 0.0],
    [0.0, 0.5, 0.0],
    [0.0, 0.0, 1.0]
], dtype=float)

# 4. Tilted Universe (Skewed Crystal Lattice) — axes no longer 90°
tilted = np.array([
    [1.0, 0.5, 0.0],
    [0.0, 1.0, 0.5],
    [0.0, 0.0, 1.0]
], dtype=float)

bases = {
    "standard":    standard,
    "rotated_z45": rotated_z45,
    "stretched":   stretched,
    "tilted":      tilted,
}

# ==========================================
# ⚡ THE ACTIONS (Standard Transformations 'M')
# ==========================================

action_rotate_x_90 = np.array([
    [1.0,  0.0,  0.0],
    [0.0,  0.0, -1.0],
    [0.0,  1.0,  0.0]
], dtype=float)

action_scale2x = np.array([
    [2.0, 0.0, 0.0],
    [0.0, 2.0, 0.0],
    [0.0, 0.0, 2.0]
], dtype=float)

action_shear_x_along_z = np.array([
    [1.0, 0.0, 1.0],
    [0.0, 1.0, 0.0],
    [0.0, 0.0, 1.0]
], dtype=float)

action_flip_z = np.array([
    [1.0,  0.0,  0.0],
    [0.0,  1.0,  0.0],
    [0.0,  0.0, -1.0]
], dtype=float)

actions = {
    "rotate_x_90":     action_rotate_x_90,
    "scale2x":         action_scale2x,
    "shear_x_along_z": action_shear_x_along_z,
    "flip_z":          action_flip_z,
}

def get_basis(name):
    """Returns the 'P' Matrix (The Basis / Coordinate System)."""
    if name not in bases:
        raise ValueError(f"Unknown basis '{name}'. Available: {list(bases.keys())}")
    return bases[name]

def get_action(name):
    """Returns the 'M' Matrix (The Transformation Action)."""
    if name not in actions:
        raise ValueError(f"Unknown action '{name}'. Available: {list(actions.keys())}")
    return actions[name]
