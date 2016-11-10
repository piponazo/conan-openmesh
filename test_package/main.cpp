#include <OpenMesh/Core/Geometry/Plane3d.hh>
#include <OpenMesh/Core/IO/MeshIO.hh>
#include <OpenMesh/Core/Mesh/TriMesh_ArrayKernelT.hh>

#include <OpenMesh/Tools/Decimater/DecimaterT.hh>
#include <OpenMesh/Tools/Decimater/ModQuadricT.hh>
#include <OpenMesh/Tools/Decimater/ModNormalFlippingT.hh>

#include <iostream>

struct OpenMeshTraits : public OpenMesh::DefaultTraits
{
        // Status flags are needed to mark entities as deleted
        VertexAttributes(OpenMesh::Attributes::Status);
        FaceAttributes(OpenMesh::Attributes::Status);
        EdgeAttributes(OpenMesh::Attributes::Status);
};

using openmesh_t 	= OpenMesh::TriMesh_ArrayKernelT<OpenMeshTraits>;

int main(int argc, char **argv)
{
    openmesh_t m_openMesh;
    std::cout << "Compile & Link OpenMesh test application correctly" << std::endl;
    return EXIT_SUCCESS;
}
