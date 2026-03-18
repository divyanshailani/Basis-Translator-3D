import bpy
import numpy as np


def animate_mesh_transformation(obj, target_matrix, frame_start=1, frame_end=180):
    """
    Shape Key lerp — identity → P_matrix applied.
    The alien lattice starts identical to standard, then morphs into its true orientation.
    Standard lattice stays fixed throughout (not animated).
    """
    M = np.array(target_matrix)
    if not obj.data.shape_keys:
        obj.shape_key_add(name="Basis")
    sk_target = obj.shape_key_add(name="Transformed")
    for i, v in enumerate(obj.data.vertices):
        orig_co = np.array([v.co.x, v.co.y, v.co.z])
        new_co  = M @ orig_co
        sk_target.data[i].co.x = new_co[0]
        sk_target.data[i].co.y = new_co[1]
        sk_target.data[i].co.z = new_co[2]
    sk_target.value = 0.0
    sk_target.keyframe_insert(data_path="value", frame=frame_start)
    sk_target.value = 1.0
    sk_target.keyframe_insert(data_path="value", frame=frame_end)


def set_cinematic_interpolation(obj):
    """Smooth Bezier curves. Handles Blender 4.4+ Action Slots and classic systems."""
    if not obj.data.shape_keys or not obj.data.shape_keys.animation_data:
        return
    action = obj.data.shape_keys.animation_data.action
    if not action:
        return
    if hasattr(action, 'layers') and action.layers:
        try:
            for layer in action.layers:
                for strip in layer.strips:
                    if hasattr(strip, 'fcurves'):
                        for fcurve in strip.fcurves:
                            for kp in fcurve.keyframe_points:
                                kp.interpolation = 'BEZIER'
        except Exception:
            pass
    elif hasattr(action, 'fcurves'):
        for fcurve in action.fcurves:
            for kp in fcurve.keyframe_points:
                kp.interpolation = 'BEZIER'


def run_director(obj, target_matrix, frame_start=1, frame_end=180):
    """Master switch — animate and smooth."""
    animate_mesh_transformation(obj, target_matrix, frame_start, frame_end)
    set_cinematic_interpolation(obj)
    print(f"🎬 ANIMATOR: Shape Key locked for {obj.name}")
