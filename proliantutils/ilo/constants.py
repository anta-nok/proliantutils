# Copyright 2017 Hewlett Packard Enterprise Development LP
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

# SUPPORTED_BOOT_MODE constants

SUPPORTED_BOOT_MODE_LEGACY_BIOS_ONLY = 'legacy bios only'
SUPPORTED_BOOT_MODE_UEFI_ONLY = 'uefi only'
SUPPORTED_BOOT_MODE_LEGACY_BIOS_AND_UEFI = 'legacy bios and uefi'
SUPPORTED_BIOS_PROPERTIES = [
    "AdvancedMemProtection",
    "AutoPowerOn",
    "BootMode",
    "BootOrderPolicy",
    "CollabPowerControl",
    "DynamicPowerCapping",
    "DynamicPowerResponse",
    "IntelligentProvisioning",
    "IntelPerfMonitoring",
    "IntelProcVtd",
    "IntelQpiFreq",
    "IntelTxt",
    "PowerProfile",
    "PowerRegulator",
    "ProcAes",
    "ProcCoreDisable",
    "ProcHyperthreading",
    "ProcNoExecute",
    "ProcTurbo",
    "ProcVirtualization",
    "SecureBootStatus",
    "Sriov",
    "ThermalConfig",
    "ThermalShutdown",
    "TpmState",
    "TpmType",
    "UefiOptimizedBoot"
]
SUPPORTED_REDFISH_BIOS_PROPERTIES = SUPPORTED_BIOS_PROPERTIES + [
    "WorkloadProfile"
]
