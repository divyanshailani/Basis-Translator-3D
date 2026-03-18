import bpy
import sys
import os
import importlib
import numpy as np

# ── 0. NUKE MEMORY CACHE ─────────────────────────────────
for module_name in list(sys.modules.keys()):
    if module_name in ['matrices', 'basis_utils', 'materials', 'scene_builder', 'animator'] \
            or module_name.startswith('utils.'):
        del sys.modules[module_name]

# ── 1. DIMENSIONAL BRIDGE ────────────────────────────────
path_phase2 = "/Users/divyanshailani/Desktop/Project_3_Basis_Translator/Phase_2 Blender"
path_phase1 = "/Users/divyanshailani/Desktop/Project_3_Basis_Translator/Phase_1_Logic"

if path_phase2 not in sys.path: sys.path.insert(0, path_phase2)
if path_phase1 not in sys.path: sys.path.insert(0, path_phase1)

from utils import materials, scene_builder, animator
import matrices, basis_utils

# ── 2. MISSION CONTROL ───────────────────────────────────
# Available bases: "standard" | "rotated_z45" | "stretched" | "tilted"
ALIEN_BASIS     = "rotated_z45"
ANCHOR_VECTOR   = np.array([2.0, 2.0, 1.5])  # The absolute physical point — never moves
GRID_SIZE       = 3
FRAME_START     = 1
FRAME_MORPH_END = 120  # 2 seconds at 60fps

print(f"\n🚀 INITIATING PROJECT 03: CHANGE OF BASIS → {ALIEN_BASIS.upper()}")

# ── 3. CLEAR THE VOID ────────────────────────────────────
scene_builder.clear_scene()
scene_builder.setup_world_lighting()

# ── 4. FETCH MATH DATA ───────────────────────────────────
P_matrix = matrices.get_basis(ALIEN_BASIS)
mats     = materials.setup_dual_materials()

# ── 5. STANDARD UNIVERSE (Fixed Ghost) ───────────────────
std_lattice = scene_builder.build_lattice("Std_Lattice", mats['std_grid'], size=GRID_SIZE)
std_i  = scene_builder.build_arrow("Std_i",  mats['std_i'],  (1, 0, 0))
std_j  = scene_builder.build_arrow("Std_j",  mats['std_j'],  (0, 1, 0))
std_k  = scene_builder.build_arrow("Std_k",  mats['std_k'],  (0, 0, 1))

# ── 6. ALIEN UNIVERSE (Morphs into true orientation) ─────
alien_lattice = scene_builder.build_lattice("Alien_Lattice", mats['alien_grid'], size=GRID_SIZE)
alien_i = scene_builder.build_arrow("Alien_i", mats['alien_i'], (1, 0, 0))
alien_j = scene_builder.build_arrow("Alien_j", mats['alien_j'], (0, 1, 0))
alien_k = scene_builder.build_arrow("Alien_k", mats['alien_k'], (0, 0, 1))

# ── 7. ANCHOR VECTOR (The Absolute Truth — Never Moves) ──
anchor = scene_builder.build_arrow("ANCHOR_VEC", mats['vector'], tuple(ANCHOR_VECTOR))

camera = scene_builder.setup_camera()

# ── 8. ANIMATE THE ALIEN UNIVERSE ────────────────────────
animator.run_director(alien_lattice, P_matrix, FRAME_START, FRAME_MORPH_END)
animator.run_director(alien_i,       P_matrix, FRAME_START, FRAME_MORPH_END)
animator.run_director(alien_j,       P_matrix, FRAME_START, FRAME_MORPH_END)
animator.run_director(alien_k,       P_matrix, FRAME_START, FRAME_MORPH_END)

bpy.context.scene.frame_end = FRAME_MORPH_END + 40

# ── 9. DEEP MATH REPORT ──────────────────────────────────
print("\n" + "="*50)
print("🌌 DIMENSIONAL TRANSLATION REPORT")
print(f"Physical Location (Standard):      {ANCHOR_VECTOR}")
alien_coords = basis_utils.express_in_basis(ANCHOR_VECTOR, P_matrix)
print(f"Alien Coordinates ({ALIEN_BASIS}): {np.round(alien_coords, 3)}")
print("="*50 + "\n")
print("🎬 3D SYSTEM ONLINE: Dual-Lattice constructed and Keyframed.")

# ── 10. EXPORT ───────────────────────────────────────────
desktop_path = os.path.join(
    os.path.expanduser("~"), "Desktop", f"Project_03_{ALIEN_BASIS}.mp4"
)
bpy.context.scene.render.filepath = desktop_path
if hasattr(bpy.context.scene.render.image_settings, 'media_type'):
    bpy.context.scene.render.image_settings.media_type = 'VIDEO'
else:
    bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
bpy.context.scene.render.ffmpeg.format = 'MPEG4'
bpy.context.scene.render.ffmpeg.codec  = 'H264'
bpy.context.scene.render.resolution_x  = 1920
bpy.context.scene.render.resolution_y  = 1080
bpy.context.scene.render.fps           = 60
print(f"🎥 EXPORT READY → {desktop_path}")
print("Render → Render Animation  (Ctrl+F12)")
