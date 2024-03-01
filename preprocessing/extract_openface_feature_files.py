### The below script - identifies all the OpenFace Facial Extraction Data files from the participant response videos
import os
import glob
import shutil

files_to_ignore = [".DS_Store"]

def extractOpenFaceFeatures(openface_dataset_path, output_path):

    participants = [participant for participant in os.listdir(openface_dataset_path) if participant not in files_to_ignore]

    ## Create a directory to store all the participant facial features .csv files
    if not os.path.exists(output_path):
        os.mkdir(output_path)

    for participant in participants:
        participant_data_path = openface_dataset_path + participant + "/"
        # Use glob to search for files with .csv extension in the specified directory
        csv_files = glob.glob(participant_data_path + "/*.csv")

        participant_output_path = output_path + "/" + participant + "/"
        ## Create a participant directory to store the facial features of the given participant
        if not os.path.exists(participant_output_path):
            os.mkdir(participant_output_path)

        for participant_feature_file in csv_files:
            ## Obtain the base name of the csv file
            csv_file_name = os.path.basename(participant_feature_file)
            output_participant_feature_file = participant_output_path + csv_file_name

            # Copy the file from source to destination
            shutil.copy(participant_feature_file, output_participant_feature_file)
            # break ## from csv files
        # break ## from participants


def main():
    video_clipping_duration = 1
    openface_features_dataset_path = "../../studyData/openface_datasets/"
    openface_cut_datasets = f"openface_cut_dataset_{video_clipping_duration}s"
    openface_cut_dataset_path = openface_features_dataset_path + openface_cut_datasets + "/"
    openface_output_path = "../../studyData/openface_datasets/facial_features_" + openface_cut_datasets + "/"

    extractOpenFaceFeatures(
        openface_dataset_path=openface_cut_dataset_path,
        output_path=openface_output_path
    )


if __name__=="__main__":
    main()