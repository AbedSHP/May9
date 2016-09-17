all_commands = {


    #------ Polygon Primitives ------#
    "Cube":"mc.polyCube()",
    "Sphere":"mc.polySphere()",
    "Plane":"mc.polyPlane()",
    "Torus":"mc.polyTorus()",
    "Cone":"mc.polyCone()",
    "Cylinder":"mc.polyCylinder()",
    "Platonic Solid":"mc.polyPlatonicSolid()",
    "Prism":"mc.polyPrism()",
    "Pyramid":"mc.polyPyramid()",
    "Pipe":"mc.polyPipe()",
    "Helix":"mc.polyHelix()",
    "Soccer Ball":"mc.CreatePolygonSoccerBall()",
    "Type":"import maya.app.type.typeToolSetup\nmaya.app.type.typeToolSetup.createTypeTool()",

    #------ NURBS Primitives ------#
    "NURBS Sphere": "mc.CreateNURBSSphere()",
    "NURBS Cube": "mc.CreateNURBSCube()",
    "NURBS Cylinder": "mc.CreateNURBSCylinder()",
    "NURBS Cone": "mc.CreateNURBSCone()",
    "NURBS Plane": "mc.CreateNURBSPlane()",
    "NURBS Torus": "mc.CreateNURBSTorus()",
    "NURBS Circle": "mc.CreateNURBSCircle()",
    "NURBS Square": "mc.CreateNURBSSquare()",

    #------ Lights ------#
    "Point Light": "mc.CreatePointLight()",
    "Directional Light": "mc.CreateDirectionalLight;()",
    "Ambient Light": "mc.CreateAmbientLight()",
    "Spot Light": "mc.CreateSpotLight()",
    "Area Light": "mc.CreateAreaLight()",
    "Volume Light": "mc.CreateVolumeLight()",

    #------ Others Primitives ------#
    "Locator": "mc.CreateLocator()",
    "Annotation": "mc.CreateAnnotateNode()",

    #------ Others ------#
    "Create Camera": "mc.CreateCameraOnly()",
    "Create Camera and Aim": "mc.CreateCameraAim()",
    "Create Camera, Aim and Up": "mc.CreateCameraAimUp()",
    "Create Stereo Camera": "import maya.app.stereo.stereoCameraRig\nmaya.app.stereo.stereoCameraRig.createStereoCameraRig()",
    "Distance Tool": "mc.DistanceTool()",

    #------ Surface Operations ------#
    "Revolve Curves": "mc.Revolve()",
    "Loft Curves": "mc.Loft()",
    "Extrude Curves": "mc.Extrude()",

    #------ Transforms ------#
    "Freeze Transformations":"mel.eval('makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;')",
    "Center Pivot":"mel.eval('CenterPivot;')",
    "Grow Selection":"mel.eval('GrowPolygonSelectionRegion;')",
    "Shrink Selection":"mel.eval('ShrinkPolygonSelectionRegion;')",
    "Combine":"mc.polyUnite()",
    "Delete History":"mel.eval('DeleteHistory;')",
    "Separate":"mc.polySeparate()",
    "Duplicate":"mc.DuplicateFace()",
    "Align Objects":"mel.eval('align -atl -x Mid -y Mid -z Mid;')",
    "Smooth Polygons":"mc.SmoothPolygon()",
    "Snap to Center of World":"mel.eval('global proc rmCenterObjects(int $ft){string $sel[] = `ls -sl`;string $obj;for ($obj in $sel){xform -cp $obj;move -rpr 0 0 0 $obj;if ($ft == 1){select -r $obj ;FreezeTransformations;makeIdentity -apply true -t 1 -r 1 -s 1 -n 0;}}select -r $sel;}rmCenterObjects(0);')",
    "Mirror +X":"mel.eval('polyMirrorFace -ws 1  -direction 0 -mergeMode 1 -ch 1;')",
    "Mirror -X":"mel.eval('polyMirrorFace -ws 1  -direction 1 -mergeMode 1 -ch 1;')",
    "Mirror +Y":"mel.eval('polyMirrorFace -ws 1  -direction 2 -mergeMode 1 -ch 1;')",
    "Mirror -Y":"mel.eval('polyMirrorFace -ws 1  -direction 3 -mergeMode 1 -ch 1;')",
    "Mirror +Z":"mel.eval('polyMirrorFace -ws 1  -direction 4 -mergeMode 1 -ch 1;')",
    "Mirror -Z":"mel.eval('polyMirrorFace -ws 1  -direction 5 -mergeMode 1 -ch 1;')",
    "Mirror Cut YZ":"mel.eval('polyMirrorCut 1 1 0.001;')",
    "Mirror Cut XZ":"mel.eval('polyMirrorCut 2 1 0.001;')",
    "Mirror Cut XY":"mel.eval('polyMirrorCut 3 1 0.001;')",

    #------ Mesh Tools ------#
    "Bridge":"mc.BridgeEdge()",
    "Bevel":"mc.polyBevel()",
    "Fill Hole":"mc.polyCloseBorder()",
    "Merge Components":"mc.polyMergeVertex()",
    "Insert Edge Loop Tools":"mc.SplitEdgeRingTool()",
    "CV Curve Tool":"mc.CVCurveTool()",
    "EP Curve Tool":"mc.EPCurveTool()",
    "Bezier Curve Tool":"mc.CreateBezierCurveTool()",
    "Pencil Curve Tool":"mc.PencilCurveTool()",
    "Create Polygon Tool": "mc.CreatePolygonTool()",
    "Multi Cut Tool": "mc.dR_multiCutTool()",
    "Add Divisions": "mc.polySubdivideFacet()",
    "Boolean Union": "mel.eval('da_interactiveUnion')",
    "Boolean Difference": "mel.eval('da_interactiveDifference')",
    "Boolean Intersection": "mel.eval('da_interactiveIntersection')",
    "Sculpt Geometry Tool": "mc.SculptGeometryTool()",
    "Merge Vertex Tool": "mc.MergeVertexTool()",
    "Target Weld Tool": "mc.dR_targetWeldTool()",
    "Fill Selection": "import maya.cmds as mc\nimport maya.mel as mel\noEdges = mc.ls(sl=True)\noObj = oEdges[0].split('.')[0]\noFace = ''\nfor i in oEdges:\n\tif '.f[' in i:\n\t\toFace = i\nmc.DetachComponent()\nmc.select(cl=True)\nmc.select(oFace)\nmc.ConvertSelectionToShell()\noFacesFinal = mc.ls(sl=True)\nmc.select(oObj)\nmc.polyMergeVertex(d=0.0001)\nmc.select(oFacesFinal)\nmc.selectType(smp=0, sme=0, smf=1, smu=0, pv=0, pe=0, pf=1, puv=0)\nmc.hilite(oObj, r=True)",
    "Append to Polygon Tool": "mc.AppendToPolygonTool()",
    "Bevel Tool": "mc.dR_bevelTool()",
    "Bridge Tool": "mc.dR_performBridge()",
    "Connect Tool": "mc.dR_connectTool()",
    "Offset Edge Loop Tool": "mc.DuplicateEdges()",
    "Quad Draw Tool": "mc.dR_quadDrawTool()",
    "Slide Edge Tool": "mc.SlideEdgeTool()",

    #------ Normals ------#
    "Reverse Normals":"mc.polyNormal()",
    "Soften Edge":"mel.eval('polySoftEdge -a 180 -ch 1;')",
    "Harden Edge":"mel.eval('polySoftEdge -a 0 -ch 1;')",

    #------ Windows ------#
    "UV Texture Editor":"mc.TextureViewWindow()",
    "Outliner":"mc.OutlinerWindow()",
    "Graph Editor":"mc.GraphEditor()",
    "Render Settings":"mel.eval('unifiedRenderGlobalsWindow;')",
    "Render View":"mc.RenderViewWindow()",
    "HyperShade":"mc.HypershadeWindow()",
    "Script Editor":"mc.ScriptEditor()",
    "Component Editor":"mc.ComponentEditor()",
    "Attribute SpreadSheet":"mc.SpreadSheetEditor()",
    "Connection Editor":"mc.ConnectionEditor()",
    "Visor":"mc.VisorWindow()",
    "Asset Editor":"mc.AssetEditor()",
    "Namespace Editor":"mc.NamespaceEditor()",
    "File Path Editor":"mc.FilePathEditor()",
    "Channel Control":"mc.ChannelControlEditor()",
    "Command Shell":"mc.CommandShell()",
    "Rendering Flags":"mc.RenderFlagsWindow()",
    "Trax Editor":"mc.CharacterAnimationEditor()",
    "Camera Sequencer":"mc.SequenceEditor()",
    "Dope Sheet Editor":"mc.DopeSheetEditor()",
    "Blend Shape Editor":"mc.BlendShapeEditor()",
    "Expression Editor":"mc.ExpressionEditor()",
    "Sets Editor":"mc.SetEditor()",
    "Deformer Set Editor":"mc.DeformerSetEditor()",
    "Character Set Editor":"mc.CharacterSetEditor()",
    "Partitions Editor":"mc.PartitionEditor()",
    "Light Linker (Light Centric)":"mc.LightCentricLightLinkingEditor()",
    "Light Linker (Object Centric)":"mc.ObjectCentricLightLinkingEditor()",
    "Preferences":"mc.PreferencesWindow()",
    "Hotkey Editor":"mc.HotkeyPreferencesWindow()",
    "Plugin Manager":"mc.PluginManager()",
    "Playblast":"mc.PlayblastOptions()",
    "Hypergraph Hierarchy":"mc.HypergraphHierarchyWindow()",
    "Hypergraph Connections":"mc.HypergraphDGWindow()",
    "Set Driven Key":"mc.SetDrivenKeyOptions()",
    "Reference Editor":"mc.ReferenceEditor()",

    #------ Animation ------#
    "Joint Tool":"mc.JointTool()",
    "IK Handle Tool":"mc.IKHandleTool()",
    "Toggle Ghosting":"import maya.mel as mel\nimport maya.cmds as mc\nobj = mc.ls(sl=1)\nshape = mc.listRelatives(obj[0])\nisGhosted = mc.getAttr(shape[0] + '.ghosting')\nif isGhosted:\n\tmc.UnghostObject()\nelse:\n\tmc.GhostObject()",
    "Connect Joints":"mc.ConnectJoint()",
    "Insert Joint Tool":"mc.InsertJointTool()",
    "Smooth Bind":"mc.SmoothBindSkin()",
    "Paint Skin Weight Tool":"mc.ArtPaintSkinWeightsTool()",
    "Create Editable Motion Trail":"mc.CreateMotionTrail()",
    "Attach to Motion Path":"mc.AttachToPath()",
    "Bake Simulation":"mc.BakeSimulationOptions()",

    #------ Deformers ------#
    "Lattice":"mc.CreateLattice()",
    "Bend":"mc.Bend()",
    "Flare":"mc.Flare()",
    "Sine":"mc.Sine()",
    "Squash":"mc.Squash()",
    "Twist":"mc.Twist()",
    "Wave":"mc.Wave()",

    #------ Constraints ------#
    "Point Constraint":"mc.PointConstraint()",
    "Parent Constraint":"mc.ParentConstraint()",
    "Orient Constraint":"mc.OrientConstraint()",
    "Scale Constraint":"mc.ScaleConstraint()",
    "Aim Constraint":"mc.AimConstraint()",
    "Pole Vector Constraint":"mc.PoleVectorConstraint()",

    #------ UVs ------#
    "Split UVs":"mc.polySplitTextureUV()",

    #------ Convert ------#
    "Convert NURBS to Polygons": "mc.NURBSToPolygons()",
    "Convert Paint Effects to Polygons": "mc.PaintEffectsToPoly()",
    "Convert Geometry to Bounding Box": "mc.GeometryToBoundingBox()",

    # ------ Misc ------#
    "Make Live": "mc.MakeLive()",
    "Make Curve Dynamic": "mc.MakeCurvesDynamic()",
    "Make Paintable": "mc.MakePaintable()",
    "Paint Effects Tool": "mc.PaintEffectsTool()",
    "Attach Brush to Curves": "mc.AttachBrushToCurves()",
    "Export All to Alembic": "mc.AlembicExportAllOptions()",
    "Export Selection to Alembic": "mc.AlembicExportSelectionOptions()",
    "Reduce": "mc.ReducePolygonOptions()",
    "Snap Together Tool": "mel.eval('setToolTo snapTogetherToolCtx;')",
    "Set Project": "mc.SetProject()",
    "Project Window": "mc.ProjectWindow()",
    "Create Reference": "mc.CreateReference()",
    "Export Selection": "mc.ExportSelectionOptions()",
    "Export All": "mc.ExportOptions()",
    "Optimize Scene Size": "mc.OptimizeSceneOptions()",
    "Import": "mc.ImportOptions()",

    #------ Custom ------#
    "Move Pivot To Vertices":"oObj = mc.ls(sl=True)[0].split('.')[0]\noClst = mc.cluster(name='envelope')[1]\nposX = mc.getAttr(str(oClst) + '.originX')\nposY = mc.getAttr(str(oClst) + '.originY')\nposZ = mc.getAttr(str(oClst) + '.originZ')\nmc.move(posX,posY,posZ, oObj + '.scalePivot', oObj + '.rotatePivot')\nmc.delete(oClst)\nmc.select(oObj)",
    "Create Locator on Selected Vertices":"oObj = mc.ls(sl=True)[0].split('.')[0]\noClst = mc.cluster(name='envelope')[1]\nposX = mc.getAttr(str(oClst) + '.originX')\nposY = mc.getAttr(str(oClst) + '.originY')\nposZ = mc.getAttr(str(oClst) + '.originZ')\nlocator = mc.spaceLocator()\nmc.move(posX,posY,posZ)\nmc.delete(oClst)\nmc.select(nlocator)",
    "Create Joints From Nulls":"oPos = []\noPosFinal = []\noSel = mc.ls(sl=True)\nfor i in range(0,len(oSel)):\n\toPos = []\n\toPos.append(mc.getAttr(oSel[i] + '.translateX'))\n\toPos.append(mc.getAttr(oSel[i] + '.translateY'))\n\toPos.append(mc.getAttr(oSel[i] + '.translateZ'))\n\toPosFinal.append(oPos)\nmc.select(cl=True)\nfor i in range(0,len(oPosFinal)):\n\tmc.joint(p=(oPosFinal[i]), radius=1)",
    "Toggle Discrete Scale": "state = mc.manipScaleContext('Scale', query=True, snap=True)\nif state:\n\tmc.manipScaleContext('Scale', edit=True, snap=False)\nelse:\n\tmc.manipScaleContext('Scale', edit=True, snap=True)",
    "Toggle Discrete Rotate": "state = mc.manipRotateContext('Rotate', query=True, snap=True)\nif state:\n\tmc.manipRotateContext('Rotate', edit=True, snap=False)\nelse:\n\tmc.manipRotateContext('Rotate', edit=True, snap=True)",
    "Toggle Discrete Move": "state = mc.manipMoveContext('Move', query=True, snap=True)\nif state:\n\tmc.manipMoveContext('Move', edit=True, snap=False)\nelse:\n\tmc.manipMoveContext('Move', edit=True, snap=True)",
    "Toggle Camera Based Selection": "state = mc.selectPref(query=True, useDepth=True)\nif state:\n\tmc.selectPref(useDepth=False)\n\tmc.selectPref(paintSelectWithDepth=False)\nelse:\n\tmc.selectPref(useDepth=True)\n\tmc.selectPref(paintSelectWithDepth=True)",

    #------ nCloth ------#
    "Make nCloth": "mel.eval('createNCloth 0;')",
    "Remove nCloth": "mel.eval('removeNCloth \"selected\";')",
    "Create nCloth Constraint from Points": "mel.eval('createNConstraint transform 0;')",
    "Make nCloth Collider": "mel.eval('makeCollideNCloth;')",
    "Make nCloth Tearable": "mel.eval('createNConstraint tearableSurface 0;')",
    "Create nCache": "mel.eval('nClothCacheOpt;')",
    "Delete nCache": "mel.eval('deleteNclothCache;')",

    #------ Bullet Physics ------#
    "Make Active Rigid Body": "RigidBody.CreateRigidBody(True).executeCommandCB()\nRigidBody.CreateRigidBody().executeCommandCB()",
    "Make Passive Rigid Body": "RigidBody.CreateRigidSet().executeCommandCB(True)",
    "Create Passive Rigid Body Object": "RigidBody.CreateRigidBody(False).executeCommandCB()\nRigidBody.CreateRigidBody().executeCommandCB()",
    "Make Soft Body": "SoftBody.CreateSoftBody.executeCommandCB()",

    #------ Hair ------#
    "Create Hair":"mc.CreateHairOptions()",
    "Paint Hair Tool":"mel.eval('paintHairTool 1;')",

    #------ Display ------#
    "Toggle Grid":"mc.ToggleGrid()",
    "Toggle PolyCount":"mc.TogglePolyCount()",
    "Toggle FrameRate":"mc.ToggleFrameRate()",
    "Show All":"mc.ShowAll()",

	#------ May9 Pro ------#
	"Color Picker":"mc.openColorEditor()",
	"Color Management On":"mc.colorManagementOn()",
	"Color Management Off":"mc.colorManagementOff()",
	"Curves form Edges":"mc.CurvesFromEdges()",
	"Layout Hypershade and Persp":"mc.layoutHypershadePersp()",
	"Layout Node Editor and Persp":"mc.layoutPerspNode()",
	"Layout UV Editor and Persp":"mc.layoutPerspUV()",
	"Layout Graph Editor and Persp":"mc.layoutPerspGraph()",
	"Layout Blend Shape Editor and Persp":"mc.layoutPerspBlendShapeEditor()",
	"Layout Pose Editor and Persp":"mc.LayoutPerspPoseEditor()",
	"Layout Component Editor and Persp":"mc.layoutPerspComponent()",
	"Layout Relationship Editor and Persp":"mc.LayoutPerspRelation()",
	"Layout Script Editor and Persp":"mc.LayoutPerspScript()",
	"Layout Single Perspective":"mc.layoutSinglePersp()",
	"Outliner in Layout":"mc.LayoutOutliner()",
	"Toggle Component and Object Mode":"mc.ToggleComponentMode()",
	"Toggle UV and Object Mode":"mc.ToggleUV()",
	"Select Object by Material":"mc.SelectObjectMaterial()",
	"Parent and Position":"mc.ParentAndPosition()",
	"Simple Connector":"mc.openSimpleConnector()",
	"Toggle Curves Visibility":"mc.ToggleNurbsCurvesVis()",
	"Toggle Nurbs Visibility":"mc.ToggleNurbsVis()",
	"Toggle Subdiv Visibility":"mc.ToggleSubVis()",
	"Toggle Poly Visibility":"mc.TogglePolyVis()",
	"Toggle Light Visibility":"mc.ToggleLightVis()",
	"Toggle Joint Visibility":"mc.ToggleJointVis()",
	"Toggle IK Handles Visibility":"mc.ToggleIkVis()",
	"Toggle Deformers Visibility":"mc.ToggleDefVis()",
	"Toggle Locator Visibility":"mc.ToggleLocVis()",
	"Content Browser":"mel.eval('ContentBrowserWindow;contentBrowserSetContext(\"WindowsMenu\", \"examples\", \"Examples/Modeling/Sculpting Base Meshes/Animals\");')",
	"Evaluation Toolkit":"mc.EvaluationToolkit()",
	"Quick Rig":"mc.QuickRigEditor()",
	"Render Setup":"mc.RenderSetupWindow()",
	"Light Editor":"mc.LightList()",
	"Render View IPR":"mc.ProgressiveIPR()",
	"TX Manager":"mc.TxManager()",
	"SkyDome Light":"mc.aiSkyDome()",
	"River Constraint":"mel.eval('djRivet')",
	"Offset Keys":"mel.eval('craOffsetKeys')",
	

}
