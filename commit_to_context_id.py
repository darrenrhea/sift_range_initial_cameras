import sys
from pathlib import Path
from print_image_in_iterm2 import print_image_in_iterm2
import pprint as pp
import better_json as bj
source_id_to_context_id = {
    "ATLvBOS_16-11-2022_PGM_ESP": "22-23_ATL_CORE",
    "ATLvSAC_23-11-2022_PGM_BAL": "22-23_ATL_CITY",
    "BKNvMEM_20-11-2022_PGM_YES": "22-23_BKN_CITY",
    "BKNvTOR_21-10-2022_PGM_YES": "22-23_BKN_CORE",
    "BOSvDAL_23-11-2022_PGM_ESP": "22-23_BOS_CORE",
    "BOSvMIA_23-05-2022_PGM_ESP": "21-22_BOS_CORE",
    "CHAvBKN_31-12-2022_PGM_BAL": "22-23_CHA_STMT",
    "CHAvIND_16-11-2022_PGM_BAL": "22-23_CHA_CORE",
    "CHAvNYK_09-12-2022_PGM_BAL": "22-23_CHA_CITY",
    "CHIvDEN_13-11-2022_PGM_NBC": "22-23_CHI_CORE",
    "CLEvCHA_18-11-2022_PGM_BAL": "22-23_CLE_CORE",
    "CLEvMEM_02-02-2023_PGM_TNT": "22-23_CLE_CORE",
    "CLEvMIN_13-11-2022_PGM_BAL": "22-23_CLE_CITY",
    "DALvPOR_12-11-2022_PGM_BAL": "22-23_DAL_CORE",
    "DALvWAS_24-01-2023_PGM_BAL": "22-23_DAL_CITY",
    "DENvDET_22-11-2022_PGM_ALT": "22-23_DEN_CORE",
    "DENvOKC_22-10-2022_PGM_ALT": "22-23_DEN_STMT",
    "DENvPHX_11-01-2023_PGM_ESP": "22-23_DEN_CITY",
    "DETvBOS_12-11-2022_PGM_BAL": "22-23_DET_STMT",
    "DETvGSW_30-10-2022_PGM_BAL": "22-23_DET_CLAS",
    "DETvLAC_26-12-2022_PGM_BAL": "22-23_DET_CORE",
    "DETvTOR_14-11-2022_PGM_BAL": "22-23_DET_CITY",
    "GSWvCLE_11-11-2022_PGM_NBC": "22-23_GSW_CITY",
    "GSWvPOR_30-12-2022_PGM_NBC": "22-23_GSW_CORE",
    "HOUvLAC_14-11-2022_PGM_ATT": "22-23_HOU_CORE",
    "HOUvMIA_15-12-2022_PGM_ATT": "22-23_HOU_CITY",
    "INDvLAL_02-02-2023_PGM_SPE": "22-23_IND_CORE",
    "LACvBKN_12-11-2022_PGM_BAL": "22-23_LAC_CITY",
    "LACvDET_17-11-2022_PGM_BAL": "22-23_LAC_STMT",
    "LACvUTA_21-11-2022_PGM_BAL": "22-23_LAC_CORE",
    "LALvPOR_30-11-2022_PGM_SPE": "22-23_LAL_CORE",
    "MEMvPHX_16-01-2023_PGM_TNT": "22-23_MEM_CORE",
    "MIAvCHA_12-11-2022_PGM_BAL": "22-23_MIA_CITY",
    "MIAvDEN_13-02-2023_PGM_BAL": "22-23_MIA_CITY",
    "MIAvPHX_14-11-2022_PGM_BAL": "22-23_MIA_CORE",
    "MILvATL_14-11-2022_PGM_BAL": "22-23_MIL_CORE",
    "MILvCLE_16-11-2022_PGM_BAL": "22-23_MIL_CITY",
    "MINvDET_31-12-2022_PGM_BAL": "22-23_MIN_CORE",
    "MINvPHX_13-01-2023_PGM_BAL": "22-23_MIN_CITY",
    "NOPvHOU_12-11-2022_PGM_BAL": "22-23_NOP_CORE",
    "NYKvORL_24-10-2022_PGM_MSG": "22-23_NYK_CORE",
    "NYKvPHI_25-12-2022_PGM_ESP": "22-23_NYK_CITY",
    "OKCvTOR_11-11-2022_PGM_BAL": "22-23_OKC_CORE",
    "ORLvCHA_14-11-2022_PGM_BAL": "22-23_ORL_CITY",
    "ORLvGSW_03-11-2022_PGM_BAL": "22-23_ORL_STMT",
    "ORLvPHX_11-11-2022_PGM_BAL": "22-23_ORL_CORE",
    "PHIvATL_12-11-2022_PGM_NBC": "22-23_PHI_CORE",
    "PHIvUTA_13-11-2022_PGM_NBC": "22-23_PHI_CITY",
    "PHXvDAL_19-10-2022_PGM_ESP": "22-23_PHX_CORE",
    "PHXvNYK_20-11-2022_PGM_BAL": "22-23_PHX_CITY",
    "PORvBKN_17-11-2022_PGM_ROO": "22-23_POR_CORE",
    "PORvCHA_26-12-2022_PGM_ROO": "22-23_POR_CORE",
    "PORvDEN_24-10-2022_PGM_ALT": "22-23_POR_CORE",
    "SACvGSW_13-11-2022_PGM_NBC": "22-23_SAC_CORE",
    "SASvCHA_19-10-2022_PGM_BAL": "22-23_SAS_CORE",
    "SASvMIL_11-11-2022_PGM_BAL": "22-23_SAS_CITY",
    "TORvGSW_18-12-2022_PGM_TSN": "22-23_TOR_CITY",
    "TORvMIA_16-11-2022_PGM_TSN": "22-23_TOR_CORE",
    "UTAvNYK_15-11-2022_PGM_ATT": "22-23_UTA_CORE",
    "UTAvPHX_18-11-2022_PGM_ATT": "22-23_UTA_CLAS",
    "WASvBKN_12-12-2022_PGM_NBC": "22-23_WAS_CITY",
    "WASvPHI_27-12-2022_PGM_NBC": "22-23_WAS_CLAS",
    "WASvUTA_12-11-2022_PGM_NBC": "22-23_WAS_CORE"
}

context_id = sys.argv[1]

num_matches = 0
for source_id, c in source_id_to_context_id.items():
    if c == context_id:
        num_matches += 1
        match = source_id

assert num_matches == 1, f"ERROR: context_id {context_id} matches {num_matches} source videos?"

source_id = match

solved_cameras_dir = Path(
    "~/input_and_output/"
).expanduser()

print(f"Apparently the source_id is {source_id}")
num_cameras = 0
for wireframe_path in solved_cameras_dir.glob(f"{source_id}*wireframe.jpg"):

    print(wireframe_path.name)
    print_image_in_iterm2(
        image_path=wireframe_path
    )
    source_and_frame_index = wireframe_path.name[:-14]
    camera_pose_path = wireframe_path.parent / f"{source_and_frame_index}_initial_camera.json"
    print(camera_pose_path)
    camera_pose = bj.load(camera_pose_path)
    pp.pprint(camera_pose)
    assert camera_pose["f"] > 0
    assert camera_pose["loc"][2] > 0
    assert camera_pose["loc"][1] < -90
    assert camera_pose["rod"][0] ** 2 + camera_pose["rod"][1] ** 2 + camera_pose["rod"][2] ** 2  < 3.14159265358979 ** 2
    num_cameras += 1 

assert (
    num_cameras == 4
), f"ERROR: why are there {num_cameras} cameras?"

confirm = input("Do all 4 of those look good?")
if confirm != "y":
    print("aborting")
    sys.exit(1)


for wireframe_path in solved_cameras_dir.glob(f"{source_id}*wireframe.jpg"):

    print(wireframe_path.name)
    print_image_in_iterm2(
        image_path=wireframe_path
    )
    source_and_frame_index = wireframe_path.name[:-14]
    camera_pose_path = wireframe_path.parent / f"{source_and_frame_index}_initial_camera.json"
    print(camera_pose_path)
    camera_pose = bj.load(camera_pose_path)
    pp.pprint(camera_pose)
    assert camera_pose["f"] > 0
    assert camera_pose["loc"][2] > 0
    assert camera_pose["loc"][1] < -90


    output_dir = Path(
        f"~/tracker/apps/floormodeling/contexts/{context_id}/frames"
    ).expanduser()
    output_dir.mkdir(exist_ok=True, parents=False)

    output_file_path = Path(
        f"~/tracker/apps/floormodeling/contexts/{context_id}/frames/{source_and_frame_index}_solved_camera.json"
    ).expanduser()

    camera_pose["name"] = source_and_frame_index
    bj.dump(
        obj=camera_pose,
        fp=output_file_path
    )
    print(f"bat {output_file_path}")


print(f"cd ~/tracker && git pull --ff-only")

print(f"cd ~/tracker/apps/floormodeling/contexts/{context_id}/frames && git add *_solved_camera.json")

print(f"git commit -m '{context_id} initial cameras for sift ranges'")

print(f"git push origin master")

dir_to_stick_initial_cameras = Path(
    "~/tracker/apps/floormodeling/contexts/22-23_UTA_CLAS/frames"
).expanduser()





