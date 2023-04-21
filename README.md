# code-build-github-to-lambda
A demo to create Code Integration from Github code to Lambda function using AWS CodeBuild

## Create Lambda function
1. Create a lambda function name `github-to-lambda-function`
2. Configure lambda function to use Python 3.10

## Create builspec.yml file

### 1. Overview of the buildspec
This is an example buildspec.yml file for AWS CodeBuild, which is a service that provides build and test capabilities for your applications. The buildspec.yml file is a YAML file that specifies the different phases of the build process, including install, build, and post_build.

Here is a breakdown of the different sections of this buildspec.yml file:

- version: 0.2: This specifies the version of the buildspec.yml file format.

- phases: This section defines the different phases of the build process.

- install: This phase installs any dependencies required for the build process. In this example, it sets the Python runtime version to 3.10 and installs the dependencies specified in the requirements.txt file using pip.

- build: This phase performs the actual build process. In this example, it zips the Lambda deployment package, which includes the dependencies installed in the previous phase and the lambda_function.py file.

- post_build: This phase runs any additional commands or actions after the build process is complete. In this example, it updates the Lambda function code with the deployment package created in the previous phase using the AWS CLI command `aws lambda update-function-code`. It also prints a message to indicate that the build process is complete.

Overall, this buildspec.yml file specifies a simple build process for a Python Lambda function. It installs dependencies, creates a deployment package, and updates the Lambda function code with the new deployment package.

### 2. Build phase explanation

Here is a breakdown of the commands used in the build phase:

1. `echo "Zipping deployment package..."`: This command simply prints a message to the console indicating that the deployment package is being created.

2. `cd lib`: This command changes the current directory to the lib directory, where the Python dependencies installed in the install phase are located.

3. `zip -r9 ../deployment_package.zip .`: This command creates a ZIP archive of the contents of the lib directory, including all subdirectories and files. The archive is named deployment_package.zip and is created in the parent directory (..) of the lib directory.

4. `cd ..`: This command changes the current directory back to the parent directory of lib.

5. `zip -g deployment_package.zip lambda_function.py`: This command adds the lambda_function.py file to the existing deployment_package.zip archive using the -g option. The -g option updates an existing ZIP archive with new files, rather than creating a new archive.

When the build phase is complete, a deployment package named deployment_package.zip is created in the parent directory of lib. The deployment package contains the Python dependencies installed in the install phase, as well as the lambda_function.py file. This deployment package can then be uploaded to AWS Lambda as a single unit.
### 3. Post Build phase explanation
Here is a breakdown of the commands used in the post_build phase:

1. `echo "Updating lambda Function..."`: This command simply prints a message to the console indicating that the Lambda function code is being updated.

2. `aws lambda update-function-code --function-name github-to-lambda-demo --zip-file fileb://deployment_package.zip`: This command uses the AWS CLI to update the Lambda function code. The `--function-name` option specifies the name of the Lambda function to update, and the `--zip-file` option specifies the location of the deployment package. The `fileb://` prefix specifies that the deployment package is a binary file.

3. `echo "DONE!!"`: This command prints a message to the console indicating that the Lambda function code has been updated successfully.

When the post_build phase is complete, the Lambda function code is updated with the new deployment package. The function will now use the updated code the next time it is invoked.

## CodeBuild Configuration
1. Create a CodeBuild project
2. For the **Source**, choose `Github`
3. [Optional] If you are not connected to Github before, choose `Connect to Github`
4. After finished the Authorization process, choose `Repository in my GitHub account`
5. Choose the repo with all the above files
6. For the **Environment**, choose Ubuntu Operating system
7. Runtime `Standard`
8. Image `aws/codebuild/standard6.0`
9. For the **Primary source webhook events**, click the checkbox `Rebuild every time a code change is pushed to this repository`
10. Choose `PUSH` event type
11. Finally, click `Create build project`

