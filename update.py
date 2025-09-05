#!/usr/bin/python3

import configparser
import os
import requests
import tarfile
import shutil
import glob

def download_and_extract_repo(owner, repo, branch, temp_dir):
    """
    Downloads the repository as a tarball and extracts it to a temporary directory.
    """
    tarball_url = f"https://github.com/{owner}/{repo}/archive/refs/heads/{branch}.tar.gz"
    tarball_path = os.path.join(temp_dir, f"{repo}-{branch}.tar.gz")

    try:
        print(f"Downloading repository from {tarball_url}...")
        with requests.get(tarball_url, stream=True) as r:
            r.raise_for_status()
            with open(tarball_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        print("Download complete.")

        print(f"Extracting {tarball_path}...")
        with tarfile.open(tarball_path, "r:gz") as tar:
            tar.extractall(path=temp_dir)
        print("Extraction complete.")

        # The extracted folder has a name like 'repo-branch', we need this path
        extracted_folder_name = f"{repo}-{branch}"
        source_repo_path = os.path.join(temp_dir, extracted_folder_name)
        
        # Clean up the downloaded tarball file immediately
        os.remove(tarball_path)
        
        return source_repo_path

    except requests.exceptions.RequestException as e:
        print(f"Error downloading repository: {e}")
        return None
    except tarfile.TarError as e:
        print(f"Error extracting tarball: {e}")
        return None


def copy_specified_files(source_repo_path, destination_path, files_to_copy):
    """
    Copies files and directories specified in the config from the source
    to the destination path.
    """
    print("Starting copy process...")
    for pattern in files_to_copy:
        # Create the full source pattern path
        source_pattern = os.path.join(source_repo_path, pattern)
        
        # Use glob to find all matching files and directories
        # The recursive=True flag handles '/**' for deep recursion if needed,
        # but os.path.join and glob handle '*' correctly for a single level.
        matched_paths = glob.glob(source_pattern, recursive=True)

        if not matched_paths:
            print(f"  - Warning: No files found for pattern: {pattern}")
            continue

        for source_path in matched_paths:
            # Calculate the relative path from the source repo root
            relative_path = os.path.relpath(source_path, source_repo_path)
            
            # Create the final destination path
            destination_file_path = os.path.join(destination_path, relative_path)
            
            # Ensure the destination directory exists
            destination_dir = os.path.dirname(destination_file_path)
            os.makedirs(destination_dir, exist_ok=True)
            
            # If it's a file, copy it. If it's a directory, copy the whole tree.
            if os.path.isfile(source_path):
                shutil.copy2(source_path, destination_file_path)
                print(f"  - Copied file: {relative_path}")
            elif os.path.isdir(source_path):
                shutil.copytree(source_path, destination_file_path, dirs_exist_ok=True)
                print(f"  - Copied directory: {relative_path}")


def main():
    """
    Main function to coordinate the download, copy, and cleanup process.
    """
    config = configparser.ConfigParser()
    config.read('config.ini')

    try:
        repo_url = config.get('github', 'repo_url')
        branch = config.get('github', 'branch')
        destination_path = config.get('local', 'destination_path')
        files_to_copy_str = config.get('files', 'files_to_copy')
        files_to_copy = [path.strip() for path in files_to_copy_str.strip().split('\n')]
    except (configparser.NoSectionError, configparser.NoOptionError) as e:
        print(f"Error reading configuration file: {e}")
        return

    try:
        owner_repo = repo_url.split('github.com/')[1].split('.git')[0]
        owner, repo = owner_repo.split('/')
    except IndexError:
        print("Invalid GitHub repository URL in config.ini")
        return

    # Create a temporary directory for the download and extraction
    temp_dir = ".temp_repo_download"
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir) # Clean up old temp dir if it exists
    os.makedirs(temp_dir)

    try:
        # Step 1: Download and extract
        source_repo_path = download_and_extract_repo(owner, repo, branch, temp_dir)
        
        if source_repo_path and os.path.exists(source_repo_path):
            # Step 2: Copy the specified files to the final destination
            copy_specified_files(source_repo_path, destination_path, files_to_copy)
            print("\nCopy process finished successfully.")
        else:
            print("\nCould not proceed with copying files due to download/extraction error.")

    finally:
        # Step 3: Clean up the temporary directory
        if os.path.exists(temp_dir):
            print("Cleaning up temporary files...")
            shutil.rmtree(temp_dir)
            print("Cleanup complete.")

if __name__ == "__main__":
    main()
