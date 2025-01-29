import os
import slicer
import zipfile
import SampleData
import urllib.request

import Lib.utils as utils

from slicer.ScriptedLoadableModule import *

# BoneReconstructionPlannerTutorial


class BoneReconstructionPlannerTutorialTest(ScriptedLoadableModuleTest):
    """
    This is the test case for your scripted module.
    Uses ScriptedLoadableModuleTest base class, available at:
    https://github.com/Slicer/Slicer/blob/main/Base/Python/slicer/ScriptedLoadableModule.py
    """

    def setUp(self):
        """Do whatever is needed to reset the state - typically a scene clear will be enough."""
        slicer.mrmlScene.Clear(0)

    def runTest(self):
        """Run as few or as many tests as needed here."""
        self.setUp()
        self.test_BoneReconstructionPlannerTutorial()

    def test_BoneReconstructionPlannerTutorial(self):
        """Tests parts of the BoneReconstructionPlannerTutorial."""
        self.Tutorial = utils.Tutorial(
            "Slicer	Bone Reconstruction Planner Tutorial",
            "Sonia Pujol, Ph.D.",
            "24/11/2024",
            "description",
        )

        self.util = utils.util()
        self.layoutManager = slicer.app.layoutManager()
        self.mainWindow = slicer.util.mainWindow()

        # Clear Output folder
        self.Tutorial.clearTutorial()
        self.Tutorial.beginTutorial()
        self.delayDisplay("Starting the test")

        # Installing Bone Reconstruction Planner
        self.runInstallingBoneReconstructionPlanner()

        # Done
        self.Tutorial.endTutorial()
        self.delayDisplay("Test passed!")
    
    def runInstallingBoneReconstructionPlanner(self):
        # 1 shot: 
        mainWindow.moduleSelector().selectModule('Welcome')
        layoutManager.setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutConventionalView)
        self.Tutorial.nextScreenshot()
        self.delayDisplay('Screenshot #1: In the Welcome screen.')

        # 2 shot:
        extensions_button = util.getNamedWidget(
            "qSlicerMainWindow/DialogToolBar/QToolButton:0"
        ).inner()
