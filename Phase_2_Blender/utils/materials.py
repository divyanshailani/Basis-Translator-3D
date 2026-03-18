import bpy

def create_emission_material(name, color_rgba, color_strength=5.0):
    """Creates a glowing neon emission material using Blender shader nodes."""
    if name in bpy.data.materials:
        bpy.data.materials.remove(bpy.data.materials[name])
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    nodes.clear()
    node_emission = nodes.new(type='ShaderNodeEmission')
    node_emission.inputs['Color'].default_value = color_rgba
    node_emission.inputs['Strength'].default_value = color_strength
    node_output = nodes.new(type='ShaderNodeOutputMaterial')
    links.new(node_emission.outputs['Emission'], node_output.inputs['Surface'])
    return mat


def setup_dual_materials():
    """
    Two distinct palettes:
    Standard = dim/ghostly (faint teal + dim RGB axes)
    Alien    = glowing/aggressive (gold lattice + neon axes)
    Anchor   = pure white (the point that never moves)
    """
    mats = {
        # 🔵 Standard Universe — ghostly baseline
        'std_grid': create_emission_material("Mat_Std_Grid", (0.0, 0.3, 0.4, 1.0), 2.0),
        'std_i':    create_emission_material("Mat_Std_i",    (0.8, 0.1, 0.1, 1.0), 3.0),
        'std_j':    create_emission_material("Mat_Std_j",    (0.1, 0.8, 0.1, 1.0), 3.0),
        'std_k':    create_emission_material("Mat_Std_k",    (0.1, 0.1, 0.8, 1.0), 3.0),

        # 🟠 Alien Universe — gold and neon aggressive
        'alien_grid': create_emission_material("Mat_Alien_Grid", (0.8, 0.5, 0.0, 1.0), 8.0),
        'alien_i':    create_emission_material("Mat_Alien_i",    (1.0, 0.8, 0.0, 1.0), 15.0),
        'alien_j':    create_emission_material("Mat_Alien_j",    (1.0, 0.0, 1.0, 1.0), 15.0),
        'alien_k':    create_emission_material("Mat_Alien_k",    (0.0, 1.0, 0.8, 1.0), 15.0),

        # ⚪ Anchor Vector — the absolute truth, never moves
        'vector': create_emission_material("Mat_Fixed_Vector", (1.0, 1.0, 1.0, 1.0), 25.0),
    }
    print("🎨 DUAL PAINT SHOP: Standard + Alien palettes loaded!")
    return mats
