import sys
argv = sys.argv
argv = argv[argv.index("--") + 1:]

import bpy
camera = argv[0] #Ortho, Cross_section, or Perspective
print(camera)
bpy.context.scene.camera = bpy.data.objects[camera]

if 'photo' in argv:
    bpy.data.collections['Annotations'].hide_render=True
    material = bpy.data.materials.get("material0")

    # accessing all the nodes in that material
    nodes = material.node_tree.nodes

    # you can find the specific node by it's name
    mix_node = nodes.get("emission_mixer")

    # available inputs of that node
    # print([x.identifier for x in noise_node.inputs])
    # ['Vector', 'W', 'Scale', 'Detail', 'Distortion']

    # change value of "Fac"
    mix_node.inputs.get("Fac").default_value = 1

elif 'topo' in argv:
    bpy.data.collections['Annotations'].hide_render=True
    # accessing the materials
    material = bpy.data.materials.get("material0")

    # accessing all the nodes in that material
    nodes = material.node_tree.nodes

    # you can find the specific node by it's name
    mix_node = nodes.get("Topo_vs_Diffuse")

    # available inputs of that node
    # print([x.identifier for x in noise_node.inputs])
    # ['Vector', 'W', 'Scale', 'Detail', 'Distortion']

    # change value of "Fac"
    mix_node.inputs.get("Fac").default_value = 0.2

elif 'annotations' in argv:
    bpy.data.collections['Annotations'].hide_render=False
    
    material = bpy.data.materials.get("material0")

    # accessing all the nodes in that material
    nodes = material.node_tree.nodes

    # you can find the specific node by it's name
    mix_node = nodes.get("emission_mixer")

    # available inputs of that node
    # print([x.identifier for x in noise_node.inputs])
    # ['Vector', 'W', 'Scale', 'Detail', 'Distortion']

    # change value of "Fac"
    mix_node.inputs.get("Fac").default_value = 0.5
    
if 'fast' in argv:
    print("running low resolution")
    bpy.context.scene.cycles.samples = 1
    bpy.data.scenes[0].render.resolution_percentage = 100
    
if 'prod' in argv:
    print("running high resolution")
    bpy.context.scene.cycles.samples = 20
    bpy.data.scenes[0].render.resolution_percentage = 400

if 'mid' in argv:
    print("running mid resolution")
    bpy.context.scene.cycles.samples = 10
    bpy.data.scenes[0].render.resolution_percentage = 200
    